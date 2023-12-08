from typing import Union
import os
import os.path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import orjson
import torch
from torch import nn
import numpy as np

app = FastAPI()

users = []
with open("app/site/nicknames.json", encoding="utf-8") as f:
    users = orjson.loads(f.read())

models_configs = []
with open("app/models.json", encoding="utf-8") as f:
    models_configs = orjson.loads(f.read())

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

class NetParams:
    def __init__(self, m_in, m_out, n) -> None:
        self.m_in = m_in
        self.m_out = m_out
        self.n = n
    
    def to_str(self):
        return f"m_in={self.m_in};m_out={self.m_out};self.n={self.n}"

class Model:
    def __init__(self, config):
        print("Parsing",config["model"]) 
        #column
        self.column = config["columnname"]
        print("Parsed column name")
        
        #remap
        remap = orjson.loads(open(config["remap"], "r", encoding="utf-8").read())
        self.index2input = {}
        self.input2index = {}
        for i, el in enumerate(remap['input']):
            self.index2input[i] = el
            self.input2index[el] = i

        self.index2output = {}
        self.output2index = {}
        for i, el in enumerate(remap['output']):
            self.index2output[i] = el
            self.output2index[el] = i
        print("Parsed remap", "input mask size " + str(len(remap['input'])), "output mask size " + str(len(remap['output'])))

        #model
        if config["type"] == "softmax" :
            self.model = SimpleNetSoftmax(len(remap['input']), len(remap['output']), NetParams(config["net_params"][0], config["net_params"][1], config["net_params"][2]))
        else:
            self.model = SimpleNetSigm(len(remap['input']), len(remap['output']), NetParams(config["net_params"][0], config["net_params"][1], config["net_params"][2]))
            
        self.model.load_state_dict(torch.load(config["model"]))
        print("Parsed model")
        #dataset
        self.inputPerUser = orjson.loads(open(config["dataset"], "r", encoding="utf-8").read())
        print("Parsed dataset")


    def process_user(self, username):
        if not username in self.inputPerUser:
            return []
        # fill input
        input_mask = np.zeros(len(self.input2index), dtype=np.float32)
        for inp in self.inputPerUser[username]:
            input_mask[inp] = 1.
        # process model
        output_mask = self.model(torch.tensor(input_mask))
        # decode output
        output_pairs = []
        norm_coef = float(torch.sum(output_mask))
        for index in range(len(output_mask)):
            el = float(output_mask[index]) / norm_coef
            output_pairs.append((self.index2output[index],el))
        output_pairs.sort(key = lambda x : -x[1])
        #create result
        result = []
        result.append(self.column)
        for i, el in enumerate(output_pairs):
            if i > 10 or int(el[1] * 100) == 0:
                break
            result.append([el[0], int(el[1] * 100)])
        return result
        
print("Parsing models")
models = []
for config in models_configs:
    models.append(Model(config))
print("Finished parsing models")

@app.get("/guess")
def process(user : str):
    if user in users:
        res = []
        for m in models:
            q = m.process_user(user)
            if q != []:
                res.append(q)
        return res
    else:
        raise HTTPException(status_code=404, detail="Item not found")

app.mount("/", StaticFiles(directory="app/site", html=True), name="site")
