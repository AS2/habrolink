import psycopg
from matplotlib import pyplot as plt


DB_NAME = "########"
DB_USER = "########"
DB_PASSWORD = "########"

conn = psycopg.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)


def LoadQuery(fileName):
    return open(f"tools/Queries/{fileName}.sql", "r").read()


def inclusion_report(hub):
    fileHub = open(f"./processed_data/rawDataHubProcessedQuick.csv", "r", encoding="utf-8")
    headerHubFull = fileHub.readline().strip().split(";")[1:]
    hub_id = headerHubFull.index(hub)
    hubCounters = [0 for hub in headerHubFull]
    hubRecord = fileHub.readline().strip().split(";")
    while len(hubRecord) == 2:
        hubs = hubRecord[1].strip().split("/")
        if str(hub_id) in hubs:
            for hub in hubs:
                hubCounters[int(hub)] += 1
        hubRecord = fileHub.readline().strip().split(";")
    fileHub.close()
    return headerHubFull, [hubCounters[i] / hubCounters[hub_id] * 100 for i, _ in enumerate(headerHubFull)]

def test_gender_hub_inclusion(capsys):
    width = 0.9
    top_k = 25
    with capsys.disabled():
        for hub in ["space", "DIY", "github"]:
            lables, percents = inclusion_report(hub)
            fig, ax1 = plt.subplots()
            lables = sorted(lables, key=lambda x: percents[lables.index(x)], reverse=True)
            percents.sort(reverse=True)
            plt.xticks(rotation=90)
            ax1.bar(lables[:top_k], percents[:top_k], width=width)
            plt.savefig(fname=f"./pics/analitics/hub_{hub}_inclussion.png", bbox_inches='tight', dpi=200)