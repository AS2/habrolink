import psycopg2
import json

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

if __name__ == "__main__":
    with open("app/models/hubs.json", "w") as f:
        json.dump(prepare_dataset("rawDataHub"), f)
    with open("app/models/bookmarks.json", "w") as f:
        json.dump(prepare_dataset("rawDataBookmarkHubs"), f)