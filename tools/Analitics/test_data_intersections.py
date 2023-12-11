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


def all(iter, pred):
    for item in iter:
        if not pred(item):
            return False
    return True


def any(iter, pred):
    for item in iter:
        if pred(item):
            return True
    return False


def calculateConditionIntersections(q_results, q_results_count):
    q_count = len(q_results)
    comb_res = [0 for i in range(2**q_count)]
    q_pointers = [0 for i in range(q_count)]
    while any(zip(q_pointers, q_results_count), lambda x: x[0] < x[1]):
        least_user_id = ""
        for i, (pointer, result) in enumerate(zip(q_pointers, q_results)):
            if pointer < len(result):
                least_user_id = result[pointer][0]
        for i, (pointer, result) in enumerate(zip(q_pointers, q_results)):
            if pointer < len(result):
                user_id = result[pointer][0]
                if user_id < least_user_id:
                    least_user_id = user_id
        indxes = []
        for i, (pointer, result) in enumerate(zip(q_pointers, q_results)):
            if pointer < len(result) and result[pointer][0] == least_user_id:
                indxes.append(i)
        for s in range(2**len(indxes)):
            left = s
            comb_idx = 0
            for i in indxes:
                mod = left % 2
                left = left // 2
                if mod != 0:
                    comb_idx += 2**i
            comb_res[comb_idx] += 1
        
        for i, (pointer, result) in enumerate(zip(q_pointers, q_results)):
            if pointer < len(result) and result[pointer][0] <= least_user_id:
                q_pointers[i] += 1
    return comb_res


def test_get_data_intersections(capsys):
    out = open("./processed_data/intersect.csv", "w+")
    with capsys.disabled():
        with conn.cursor() as cur:
            conditions = [
                (LoadQuery("usersParsed"), "User parsed"),
                (LoadQuery("usersWithSpeciality"), "Speciality"),
                (LoadQuery("usersWithSpecialization"), "Specialization"),
                (LoadQuery("usersWithHub"), "Hub"),
                (LoadQuery("usersWithSkills"), "Skills"),
                (LoadQuery("usersWithWorkplace"), "Workplace"),
                (LoadQuery("usersWithPosts"), "Posts"),
                (LoadQuery("usersWithBookmark"), "Bookmark"),
                (LoadQuery("usersWithComments"), "Comments"),
            ]
            q_count = len(conditions)
            print("requesting db")
            q_results = [
                cur.execute(condition[0]).fetchall()
                for condition in conditions
                ]
            q_results_count = [ len(res)
                for res in q_results
            ]
            print("calculating intersections")
            comb_res = calculateConditionIntersections(q_results, q_results_count)
            for cond in conditions:
                out.write(cond[1] + ";")
            out.write("Count\n")
            for s, cr in enumerate(comb_res):
                left = s
                for i in range(q_count):
                    mod = left % 2
                    left = left // 2
                    if mod != 0:
                        out.write("+;")
                    else:
                        out.write(" ;")
                out.write(str(cr) + "\n")
    out.close()
