import psycopg

DB_NAME = "########"
DB_USER = "########"
DB_PASSWORD = "########"

conn = psycopg.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)


def LoadQuery(fileName):
    return open(f"tools/Queries/{fileName}.sql", "r").read()


def printRecord(out, record):
    out.write(record[0])
    for i, item in enumerate(record[1]):
        if i == 0:
            out.write(";")
        else:
            out.write("/")
        out.write(str(record[1][item]))
    out.write("\n")


def test_process_raw_data():
    quaries = [
            (LoadQuery("rawDataSpecialization"), "rawDataSpecialization"),
            (LoadQuery("rawDataHub"), "rawDataHub"),
            (LoadQuery("rawDataBookmarkHubs"), "rawDataBookmarkHubs"),
        ]
    with conn.cursor() as cur:
        for q in quaries:
            cache_file = None
            out = None
            try:
                cache_file = open(f"./processed_data/{q[1]}.csv", "r", encoding="utf-8")
            except FileNotFoundError:
                out = open(f"./processed_data/{q[1]}.csv", "w+", encoding="utf-8")
                cur.execute(q[0])
            counter = 0
            headers = {}
            res = None
            if cache_file:
                res = cache_file.readline().strip().split(";")
            else:
                res = cur.fetchone()
            while res and len(res) == 2:
                if out:
                    out.write(f"{res[0]};{res[1]}\n")
                if not res[1] in headers:
                    headers[res[1]] = counter
                    counter += 1
                if cache_file:
                    res = cache_file.readline().strip().split(";")
                else:
                    res = cur.fetchone()
            if out:
                out.close()
            if cache_file:
                cache_file.close()
            cache_file = open(f"./processed_data/{q[1]}.csv", "r", encoding="utf-8")
            out = open(f"./processed_data/{q[1]}ProcessedQuick.csv", "w+", encoding="utf-8")
            out.write("user_id")
            for header in headers:
                out.write(f";{header}")
            out.write("\n")
            res = cache_file.readline().strip().split(";")
            record = ["", {}]
            while len(res) == 2:
                if record[0] != res[0]:
                    if record[0] != "":
                        printRecord(out, record)
                    record = [res[0], {}]
                record[1][res[1]] = headers[res[1]]
                res = cache_file.readline().strip().split(";")
            printRecord(out, record)
            
            if out:
                out.close()


def test_make_datasets():
    quaryRes = ("Specialization", "rawDataSpecializationProcessedQuick")
    quariesSrc = [
            ("Hub", "rawDataHubProcessedQuick"),
            ("BookmarkHubs", "rawDataBookmarkHubsProcessedQuick"),
        ]
    with conn.cursor() as cur:
        for q in quariesSrc:
            fileSpec = open(f"./processed_data/{quaryRes[1]}.csv", "r", encoding="utf-8")
            fileHub = open(f"./processed_data/{q[1]}.csv", "r", encoding="utf-8")
            out = open(f"./{quaryRes[0]}From{q[0]}.csv", "w+", encoding="utf-8")
            headerSpecFull = fileSpec.readline().strip().split(";")[1:]
            headerHubFull = fileHub.readline().strip().split(";")[1:]
            headerSpecCounter = {}
            for i, spec in enumerate(headerSpecFull):
                headerSpecCounter[i] = 0
            headerHubCounter = {}
            for i, hub in enumerate(headerHubFull):
                headerHubCounter[i] = 0
            specRecord = fileSpec.readline().strip().split(";")
            hubRecord = fileHub.readline().strip().split(";")
            while len(specRecord) == 2 and len(hubRecord) == 2:
                if specRecord[0] == hubRecord[0]:
                    specs = specRecord[1].strip().split("/")
                    for spec in specs:
                        headerSpecCounter[int(spec)] += 1
                    hubs = hubRecord[1].strip().split("/")
                    for hub in hubs:
                        headerHubCounter[int(hub)] += 1
                    specRecord = fileSpec.readline().strip().split(";")
                    hubRecord = fileHub.readline().strip().split(";")
                elif specRecord[0] < hubRecord[0]:
                    specRecord = fileSpec.readline().strip().split(";")
                else:
                    hubRecord = fileHub.readline().strip().split(";")
            counter = 0
            headerSpecRemap = {}
            for i, spec in enumerate(headerSpecFull):
                if headerSpecCounter[i] != 0:
                    headerSpecRemap[i] = counter
                    if counter != 0:
                        out.write(";")
                    out.write(f"{spec}")
                    counter += 1
            out.write("\n")
            counter = 0
            headerHubRemap = {}
            for i, hub in enumerate(headerHubFull):
                if headerHubCounter[i] != 0:
                    headerHubRemap[i] = counter
                    if counter != 0:
                        out.write(";")
                    out.write(f"{hub}")
                    counter += 1
            out.write("\n")
            fileSpec.close()
            fileHub.close()
            fileSpec = open(f"./processed_data/{quaryRes[1]}.csv", "r", encoding="utf-8")
            fileHub = open(f"./processed_data/{q[1]}.csv", "r", encoding="utf-8")
            fileSpec.readline()
            fileHub.readline()
            specRecord = fileSpec.readline().strip().split(";")
            hubRecord = fileHub.readline().strip().split(";")
            while len(specRecord) == 2 and len(hubRecord) == 2:
                if specRecord[0] == hubRecord[0]:
                    out.write(f"{specRecord[0]}")
                    specs = specRecord[1].strip().split("/")
                    hubs = hubRecord[1].strip().split("/")
                    for i, spec in enumerate(specs):
                        if i == 0:
                            out.write(";")
                        else:
                            out.write("/")
                        out.write(str(headerSpecRemap[int(spec)]))
                    for i, hub in enumerate(hubs):
                        if i == 0:
                            out.write(";")
                        else:
                            out.write("/")
                        out.write(str(headerHubRemap[int(hub)]))
                    out.write("\n")

                    specRecord = fileSpec.readline().strip().split(";")
                    hubRecord = fileHub.readline().strip().split(";")
                elif specRecord[0] < hubRecord[0]:
                    specRecord = fileSpec.readline().strip().split(";")
                else:
                    hubRecord = fileHub.readline().strip().split(";")
            fileSpec.close()
            fileHub.close()
            out.close()