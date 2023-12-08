import psycopg2
import orjson

DB_NAME = "habrolinkdb"
DB_USER = "postgres"
DB_PASSWORD = "12345"

conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)

def LoadQuery(fileName):
    return open(f"../tools/Queries/{fileName}.sql", "r").read()

def prepare_dataset(query):
    userToHub = {}
    with conn.cursor() as cur:
        print("execute start")
        cur.execute(LoadQuery(query))
        print("execute end")
        while True:
            rows = cur.fetchmany(5000)
            print(len(rows), "processed")
            if not rows:
                break

            for row in rows:
                if not (row[0] in userToHub):
                    userToHub[row[0]] = []
                userToHub[row[0]].append(row[1])
    return userToHub

def remap_dataset(dataset, remap):
    index2input = {}
    input2index = {}
    for i, el in enumerate(remap['input']):
        index2input[i] = el
        input2index[el] = i
    print("start remapping")
    for entry in dataset:
        to_del = []
        for idx, inp in enumerate(dataset[entry]):
            if not inp in input2index:
                print("No remapping for", inp)
                to_del.append(idx)
                continue
            dataset[entry][idx] = input2index[inp]
        to_del.reverse()
        for idx in to_del:
            del dataset[entry][idx]
    print("finished remapping")
    return dataset

if __name__ == "__main__":
    with open("app/models/hubs.json", "wb") as f:
        dataset = prepare_dataset("rawDataHub")
        remap = orjson.loads(open("app/models/hubs_remap.json", "r", encoding="utf-8").read())
        f.write(orjson.dumps(remap_dataset(dataset, remap)))
    with open("app/models/bookmarks.json", "wb") as f:
        dataset = prepare_dataset("rawDataBookmarkHubs")
        remap = orjson.loads(open("app/models/bookmarks_remap.json", "r", encoding="utf-8").read())
        f.write(orjson.dumps(remap_dataset(dataset, remap)))