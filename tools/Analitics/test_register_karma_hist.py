import psycopg
from matplotlib import pyplot as plt
import numpy as np
import datetime


DB_NAME = "########"
DB_USER = "########"
DB_PASSWORD = "########"

conn = psycopg.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)


def LoadQuery(fileName):
    return open(f"tools/Queries/{fileName}.sql", "r").read()


def test_register_date_karma_hist(capsys):
    registerDate = LoadQuery("registerDate")
    registerDatePositiveKarma = LoadQuery("registerDatePositiveKarma")
    registerDateZeroKarma = LoadQuery("registerDateZeroKarma")
    registerDateNegativeKarma = LoadQuery("registerDateNegativeKarma")

    with capsys.disabled():
        with conn.cursor() as cur:
            fig, ax1 = plt.subplots()
            cur.execute(registerDate)
            res = cur.fetchall()
            y = np.array([t[0].timestamp() for t in res])
            print(len(res))
            years = [x for x in range(2006, 2025)]
            
            hist_all = np.histogram(y, 18, (datetime.datetime(2006, 1, 1).timestamp(), datetime.datetime(2024, 1, 1).timestamp()))


            bottom = np.zeros(len(hist_all[0]))
            
            cur.execute(registerDateNegativeKarma)
            res = cur.fetchall()
            y = np.array([t[0].timestamp() for t in res])
            print(len(res))
            hist_negative = np.histogram(y, 18, (datetime.datetime(2006, 1, 1).timestamp(), datetime.datetime(2024, 1, 1).timestamp()))
            hist_n = hist_negative[0]
            ax1.bar(years[:-1], hist_n, width=np.diff(years), align="edge", color=(1,0,0,0.5), bottom=bottom)
            bottom += hist_n

            cur.execute(registerDatePositiveKarma)
            res = cur.fetchall()
            y = np.array([t[0].timestamp() for t in res])
            print(len(res))
            hist_positive = np.histogram(y, 18, (datetime.datetime(2006, 1, 1).timestamp(), datetime.datetime(2024, 1, 1).timestamp()))
            hist_p = hist_positive[0]
            ax1.bar(years[:-1], hist_p, width=np.diff(years), align="edge", color=(0,1,0,0.5), bottom=bottom)
            bottom += hist_p

            cur.execute(registerDateZeroKarma)
            res = cur.fetchall()
            y = np.array([t[0].timestamp() for t in res])
            print(len(res))
            
            hist_zero = np.histogram(y, 18, (datetime.datetime(2006, 1, 1).timestamp(), datetime.datetime(2024, 1, 1).timestamp()))
            hist_z = hist_zero[0]
            ax1.bar(years[:-1], hist_z, width=np.diff(years), align="edge", color=(0,0,1,0.5), bottom=bottom)
            bottom += hist_z

            
            ax1.bar(years[:-1], hist_all[0], width=np.diff(years), edgecolor="black", align="edge", color=(0,0,1,0))

            fig.tight_layout()
            plt.show()
