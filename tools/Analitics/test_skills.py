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


def test_skills(capsys):
    width = 0.9
    top_k = 25
    q = LoadQuery("skills")
    with capsys.disabled():
        with conn.cursor() as cur:
            cur.execute(q)
            res = cur.fetchall()
            fig, ax1 = plt.subplots()
            plt.xticks(rotation=90)
            ax1.bar([r[0] for r in res][:top_k], [r[1] for r in res][:top_k], width=width)
            plt.savefig(fname=f"./pics/analitics/skills.png", bbox_inches='tight', dpi=200)
