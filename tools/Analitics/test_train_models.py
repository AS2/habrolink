from matplotlib import pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset, SubsetRandomSampler
import numpy as np
from sklearn.model_selection import KFold

class SpetialityFromHubDataset(Dataset):
    def __init__(self, src) -> None:
        super().__init__()
        self.source = src
        self.dict_user_id = []
        self.data_specialization_lists = []
        self.data_hub_lists = []
        file = open(f"./{self.source}.csv", "r", encoding="utf-8")
        self.dict_specialization_id = file.readline().strip().split(";")
        self.dict_hub_id = file.readline().strip().split(";")
        record = file.readline().strip().split(";")
        while len(record) == 3:
            self.dict_user_id.append(record[0])
            self.data_specialization_lists.append([int(x) for x in record[1].split("/")])
            self.data_hub_lists.append([int(x) for x in record[2].split("/")])
            record = file.readline().strip().split(";")
    
    def __len__(self):
        return len(self.dict_user_id)

    def __getitem__(self, idx):
        specialization_mask = np.zeros(len(self.dict_specialization_id), dtype=np.float32)
        hub_mask = np.zeros(len(self.dict_hub_id), dtype=np.float32)
        for specialization_idx in self.data_specialization_lists[idx]:
            specialization_mask[specialization_idx] = 1.
        for hub_idx in self.data_hub_lists[idx]:
            hub_mask[hub_idx] = 1.
        return idx, hub_mask, specialization_mask


class SimpleNetSigm(nn.Module):
    def __init__(self, in_f, out_f, params):
        super().__init__()
        layers = []
        layers.append(nn.Linear(in_f, int(in_f * params.m_in)))
        for i in range(params.n):
            layers.append(nn.Linear(int((in_f * params.m_in * (params.n - i) + out_f * params.m_out * i)/params.n), int((in_f * params.m_in * (params.n - (i + 1)) + out_f * params.m_out * (i + 1))/params.n)))
            layers.append(nn.ReLU())
        layers.append(nn.Linear(int(out_f * params.m_out), out_f))
        layers.append(nn.Sigmoid())
        self.layers = nn.Sequential(
            *layers
        )
    
    def forward(self, x):
        '''Forward pass'''
        return self.layers(x)


class SimpleNetSoftmax(nn.Module):
    def __init__(self, in_f, out_f, params):
        super().__init__()
        layers = []
        layers.append(nn.Linear(in_f, int(in_f * params.m_in)))
        for i in range(params.n):
            layers.append(nn.Linear(int((in_f * params.m_in * (params.n - i) + out_f * params.m_out * i)/params.n), int((in_f * params.m_in * (params.n - (i + 1)) + out_f * params.m_out * (i + 1))/params.n)))
            layers.append(nn.ReLU())
        layers.append(nn.Linear(int(out_f * params.m_out), out_f))
        layers.append(nn.Softmax(1))
        self.layers = nn.Sequential(
            *layers
        )
    
    def forward(self, x):
        '''Forward pass'''
        return self.layers(x)


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
def reset_weights(m):
    '''
        Try resetting model weights to avoid
        weight leakage.
    '''
    for layer in m.children():
        if hasattr(layer, 'reset_parameters'):
            print(f'Reset trainable parameters of layer = {layer}')
            layer.reset_parameters()

class NetParams:
    def __init__(self, m_in, m_out, n) -> None:
        self.m_in = m_in
        self.m_out = m_out
        self.n = n
    
    def to_str(self):
        return f"m_in={self.m_in};m_out={self.m_out};self.n={self.n}"

def accuracy_test(dataloader, network):
    correct, total = 0, 0
    # Iterate over the test data and generate predictions
    for i, data in enumerate(dataloader, 0):
        id, inputs, targets = data
        outputs = network(inputs.to(device=device))
        predicted = outputs.data.to(device="cpu")
        total += predicted.size(0)
        _, ind = torch.topk(predicted, 1)
        correct += targets.gather(dim=1, index=ind).sum().item()
    return correct / total

class Test:
    def __init__(self, src, k_folds, num_epochs, lr, loss_function, batch_size, mini_batch, net, net_params) -> None:
        self.src = src
        self.k_folds = k_folds
        self.num_epochs = num_epochs
        self.lr = lr
        self.loss_function = loss_function
        self.batch_size = batch_size
        self.mini_batch = mini_batch
        self.net = net
        self.net_params = net_params

        self.new_src = True
        self.new_net = True

        self.dataset = None
    
    def to_str(self):
        return f"src={self.src};k_folds={self.k_folds};num_epochs={self.num_epochs};lr={self.lr};loss_function={type(self.loss_function).__name__};batch_size={self.batch_size};mini_batch={self.mini_batch};net={type(self.net).__name__};net_params=({self.net_params.to_str()})"

    def run(self):
        x = []
        y_test = []
        y_train = []
        results_test = {}
        results_train = {}
        torch.manual_seed(42)

        if self.new_src:
            self.dataset = SpetialityFromHubDataset(self.src)
            self.new_src = False
        
        # Define the K-fold Cross Validator
        kfold = KFold(n_splits=self.k_folds, shuffle=True)
        print('--------------------------------')
        # K-fold Cross Validation model evaluation
        for fold, (train_ids, test_ids) in enumerate(kfold.split(self.dataset)):
            x.append([])
            y_test.append([])
            y_train.append([])
            print(f'FOLD {fold}')
            print('--------------------------------')
            
            train_subsampler = SubsetRandomSampler(train_ids)
            test_subsampler = SubsetRandomSampler(test_ids)
            
            trainloader = DataLoader(
                            self.dataset, 
                            batch_size=self.batch_size, sampler=train_subsampler)
            testloader = DataLoader(
                            self.dataset,
                            batch_size=self.batch_size, sampler=test_subsampler)
            
            if self.new_net:
                network = self.net(len(self.dataset.dict_hub_id), len(self.dataset.dict_specialization_id), self.net_params)
            network.to(device=device)
            network.zero_grad()
            network.apply(reset_weights)
            optimizer = torch.optim.Adam(network.parameters(), lr=self.lr)
            for epoch in range(0, self.num_epochs):
                print(f'Starting epoch {epoch+1}')
                current_loss = 0.0
                for i, data in enumerate(trainloader, 0):
                    id, inputs, targets = data
                    inputs = inputs.to(device=device)
                    targets = targets.to(device=device)
                    if type(self.loss_function).__name__ == "CrossEntropyLoss":
                        targets = torch.softmax(targets, 1)
                    optimizer.zero_grad()
                    outputs = network(inputs)
                    loss = self.loss_function(outputs, targets)
                    loss.backward()
                    optimizer.step()
                    # Print statistics
                    current_loss += loss.item()
                    if i % self.mini_batch == (self.mini_batch-1):
                        print('Loss after mini-batch %5d: %f' %
                            (i + 1, current_loss / self.mini_batch))
                        current_loss = 0.0
                # Print about testing
                print('Epoch testing')
                with torch.no_grad():
                    accuracy = accuracy_test(testloader, network)
                    accuracy_train = accuracy_test(trainloader, network)
                    print('Accuracy test: %f %%' % (100.0 * accuracy))
                    print('Accuracy train: %f %%' % (100.0 * accuracy_train))
                    x[fold].append(epoch)
                    y_test[fold].append(accuracy)
                    y_train[fold].append(accuracy_train)
            
            print('Training process has finished. Saving trained model.')
            save_path = f'./{self.to_str()};fold={fold}.pth'
            torch.save(network.state_dict(), save_path)
            
            print('Starting testing')
            with torch.no_grad():
                accuracy = accuracy_test(testloader, network)
                accuracy_train = accuracy_test(trainloader, network)
                x[fold].append(epoch)
                y_test[fold].append(accuracy)
                y_train[fold].append(accuracy_train)
                print('Accuracy test for fold %d: %f %%' % (fold, 100.0 * accuracy))
                print('Accuracy train for fold %d: %f %%' % (fold, 100.0 * accuracy_train))
                print('--------------------------------')
                results_test[fold] = 100.0 * (accuracy)
                results_train[fold] = 100.0 * (accuracy_train)
        
        plt.figure()
        for fold in range(self.k_folds):
            plt.plot(x[fold], y_test[fold])
        for fold in range(self.k_folds):
            plt.plot(x[fold], y_train[fold], linestyle='dashed')
        plt.savefig(fname=f"./{self.to_str()}.png")

        # Print fold results
        print(f'K-FOLD CROSS VALIDATION RESULTS FOR {self.k_folds} FOLDS')
        print('--------------------------------')
        sum = 0.0
        for key, value in results_test.items():
            print(f'Fold {key}: {value} %')
            sum += value
        print(f'Average test: {sum/len(results_test.items())} %')
        sum = 0.0
        for key, value in results_train.items():
            print(f'Fold {key}: {value} %')
            sum += value
        print(f'Average train: {sum/len(results_train.items())} %')

import gc

def test_multiclass_or_lables(capsys):
    with capsys.disabled():
        print(f"Using {device} device")
        for src in ["SpecializationFromHub", "SpecializationFromBookmarkHubs"]:
            for loss_function, net in zip([nn.BCELoss(), nn.CrossEntropyLoss()], [SimpleNetSigm, SimpleNetSoftmax]):
                torch.cuda.empty_cache()
                gc.collect()
                torch.cuda.empty_cache()
                Test(src=src,
                    k_folds=5,
                    num_epochs=50,
                    lr=1e-4,
                    loss_function=loss_function,
                    batch_size=100,
                    mini_batch=50,
                    net=net,
                    net_params=NetParams(
                        m_in = 0.25,
                        m_out = 3,
                        n = 1,
                        )
                    ).run()

        
def test_layers_count(capsys):
    with capsys.disabled():
        print(f"Using {device} device")
        for src in ["SpecializationFromHub", "SpecializationFromBookmarkHubs"]:
            for n in range(1, 7):
                torch.cuda.empty_cache()
                gc.collect()
                torch.cuda.empty_cache()
                Test(src=src,
                    k_folds=5,
                    num_epochs=50,
                    lr=1e-4,
                    loss_function=nn.BCELoss(),
                    batch_size=100,
                    mini_batch=50,
                    net=SimpleNetSigm,
                    net_params=NetParams(
                        m_in = 0.25,
                        m_out = 3,
                        n = n,
                        )
                    ).run()