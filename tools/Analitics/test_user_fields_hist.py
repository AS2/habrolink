import psycopg2
from matplotlib import pyplot as plt
import numpy as np

queries = [
    ["TOTAL","SELECT COUNT(*) FROM users;"],
    ["fullname","SELECT COUNT(*) FROM users WHERE fullname != '';"],
    ["avatar","SELECT COUNT(*) FROM users WHERE avatar != '';"],
    ["speciality","SELECT COUNT(*) FROM users WHERE speciality != '';"],
    ["gender","SELECT COUNT(*) FROM users WHERE gender != 0;"],
    ["last_activity","SELECT COUNT(*) FROM users WHERE last_activity != '1000-01-01 00:00:00 +00:00';"],
    ["birthday","SELECT COUNT(*) FROM users WHERE birthday != '1000-01-01';"],
    ["city","SELECT COUNT(*) FROM users WHERE location_city != ''"],
    ["region","SELECT COUNT(*) FROM users WHERE location_region != ''"],
    ["country","SELECT COUNT(*) FROM users WHERE location_country != ''"],
    ["invited_by","SELECT COUNT(*) FROM users WHERE invited_by != ''"],
    ["invited_at","SELECT COUNT(*) FROM users WHERE invited_at != '1000-01-01 00:00:00 +00:00';"],
    ["salary","SELECT COUNT(salary) FROM public.users;"],
    ["qualification","SELECT COUNT(*) FROM users WHERE qualification != ''"],
    ["bookmarks","SELECT COUNT(*) FROM (SELECT user_id as user_id FROM public.\"userToBookmark\" GROUP BY (user_id) ORDER BY user_id)"],
    ["hubs","SELECT COUNT(*) FROM (SELECT user_id FROM public.\"userToHub\" GROUP BY (user_id) ORDER BY user_id)"],
    ["posts","SELECT COUNT(*) FROM (SELECT author as user_id FROM public.\"posts\" GROUP BY (user_id) ORDER BY user_id)"],
    ["skills","SELECT COUNT(*) FROM (SELECT user_id FROM public.\"userToSkill\" GROUP BY (user_id) ORDER BY user_id)"],
    ["specializion","SELECT COUNT(*) FROM (select user_id from public.\"userToSpecialization\" group by user_id ORDER BY user_id)"],
    ["workplace","SELECT COUNT(*) FROM (SELECT user_id FROM public.\"userToWorkplace\" GROUP BY user_id ORDER BY user_id)"]
]

results = [
    ["TOTAL", 1466403],
    ["fullname", 201773],
    ["avatar", 139852],
    ["speciality", 131010],
    ["gender", 224594],
    ["lastActiv", 1316598],
    ["birthday", 163791],
    ["city", 152630],
    ["region", 169406],
    ["country", 211637],
    ["inviteBy", 37609],
    ["inviteAt", 61173],
    ["salary", 18643],
    ["qualification", 39007],
    ["bookmarks", 320435],
    ["hubs", 830947],
    ["posts", 50279],
    ["skills", 42267],
    ["specializion", 55221],
    ["workplace", 7967]
]

conn = psycopg2.connect(
            dbname="habrolinkdb",
            user="postgres",
            password="12345")

with conn.cursor() as cur:
    results = []
    for query in queries:
        cur.execute(query[1])
        data = cur.fetchall()[0][0]
        print(query[0], data)
        results.append([query[0], data])
    print(results)
    results.sort(key = lambda x : -x[1])
    names, vals =  zip(*results)

    fig, ax = plt.subplots(1, 1) 
    ax.bar([i for i in range(len(vals))], vals)
  
    # Set title 
    #ax.set_title("Title") 
  
    # adding labels 
    ax.set_xlabel('Fields') 
    ax.set_ylabel('User count') 
  
    # Make some labels. 
    rects = ax.patches 
    labels = names 
  
    for i, (rect, label) in enumerate(zip(rects, labels)):
        height = rect.get_height() 
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label, 
            ha='center', va='bottom') 
        if (int(vals[i] / vals[0] * 100) >= 5):
            ax.text(rect.get_x() + rect.get_width() / 2, height / 2 - 0.01, str(int(vals[i] / vals[0] * 100)) + "%", 
                ha='center', va='bottom', color="white") 
    plt.show()