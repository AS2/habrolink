# this script will get all data we want, and send it to database.
import psycopg2
import argparse
import os
import os.path
from requester import get_user, get_post
import time

def habrTimeToPostgreTime(t):
	if t == "":
		return "1000-01-01 00:00:00 +00:00"
	# input string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second
	# postgres YYYY-MM-DD hh:mm:ss +00:00
	return t[0:10] + " " + t[11:19] + " " + t[19:]

def habrDateToPostgreDate(t):
	if t == "":
		return "1000-01-01"
	# postgres YYYY-MM-DD
	return t

# this function will push one post to database
def add_one_post(post, db_cursor):	
	# add to main table	
	db_cursor.execute("INSERT INTO posts("
	"id, creation_time, is_corp, lang, title,"
	"type, author, comments_count, favorites_count, reading_count,"
	"score, votes_up, votes_down, votes_count, reading_minutes)"
	" VALUES("
	"%s, %s, %s, %s, %s, "
	"%s, %s, %s, %s, %s, "
	"%s, %s, %s, %s, %s)",
	(post["id"], habrTimeToPostgreTime(post["time"]), post["is_corp"], post["lang"], post["title"],
	post["type"], post["author"], post["comments_count"], post["favorites_count"], post["reading_count"],
	post["score"], post["votes_up"], post["votes_down"], post["votes_count"], post["reading_minutes"]))

	# add to postToTag table
	for elem in post["tags"]:
		db_cursor.execute("INSERT INTO public.\"postToTag\"(post_id, tag) VALUES(%s, %s)", (post["id"], elem))

	# add to postToHub table
	for elem in post["hubs"]:
		db_cursor.execute("INSERT INTO public.\"postToHub\"(post_id, hub_id) VALUES(%s, %s)", (post["id"], elem))

# this function will push one user to database
def add_one_user(user, db_cursor):	
	# for multiple users we can do executemany.

	# add to main table	
	db_cursor.execute("INSERT INTO users("
	"id, fullname, avatar, speciality, gender,"
	"rating, karma, karma_votes_amount, last_activity, register, "
	"birthday, is_readonly, invited, location_city, location_region, "
	"location_country, invited_by, invited_at, salary, currency, "
	"qualification)"
	" VALUES("
	"%s, %s, %s, %s, %s, "
	"%s, %s, %s, %s, %s, "
	"%s, %s, %s, %s, %s, "
	"%s, %s, %s, %s, %s, "
	"%s)",
	(user["id"], user["fullname"], user["avatar"], user["speciality"], user["gender"],
	user["rating"], user["karma"], user["karma_votes_amount"], habrTimeToPostgreTime(user["last_activity"]), habrTimeToPostgreTime(user["register"]),
	habrDateToPostgreDate(user["birthday"]), user["is_readonly"], user["invited"], user["location_city"], user["location_region"],
	user["location_country"], user["invited_by"], habrTimeToPostgreTime(user["invited_at"]), user["salary"], user["currency"],
	user["qualification"]))
	
	# add to userToWorkplace table
	for elem in user["workplace"]:
		db_cursor.execute("INSERT INTO public.\"userToWorkplace\"(user_id, workplace_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToSpecialization table
	for elem in user["specializations"]:
		db_cursor.execute("INSERT INTO public.\"userToSpecialization\"(user_id, specialization_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToSkill table
	for elem in user["skills"]:
		db_cursor.execute("INSERT INTO public.\"userToSkill\"(user_id, skill_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToInvite table
	for elem in user["invites"]:
		db_cursor.execute("INSERT INTO public.\"userToInvite\"(parent_id, child_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToHub table
	for elem in user["hubs"]:
		db_cursor.execute("INSERT INTO public.\"userToHub\"(user_id, hub_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToPost table
	for elem in user["posts"]:
		db_cursor.execute("INSERT INTO public.\"userToPost\"(user_id, post_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToBookmark table
	for elem in user["bookmarks"]:
		db_cursor.execute("INSERT INTO public.\"userToBookmark\"(user_id, post_id) VALUES(%s, %s)", (user["id"], elem))

	# add to userToFollowers table
	for elem in user["followers"]:
		db_cursor.execute("INSERT INTO public.\"userToFollow\"(parent_id, follower_id) VALUES(%s, %s)", (user["id"], elem))
	
if __name__ == "__main__":
	# parse arguments
	parser = argparse.ArgumentParser(prog='Dumper from habr to postgres')
	parser.add_argument("--mode", choices=["posts", "users"], help="dumper mode")
	parser.add_argument("--users", type=str, help="path to file, which contail all users names")
	parser.add_argument("--index", type=int, help="index of this dumper")
	parser.add_argument("--count", type=int, help="total count of dumpers")
	args = parser.parse_args()

	# load all user names
	if not os.path.isfile(args.users):
		print("Error!", args.users, "not exist")
	else:	
		usernames = []
		with open(args.users, "rt") as f:
			usernames = f.read().split('\n')		
		print("Start worker", args.index, "out of", args.count, "for dumping", args.mode)
		#connect to db
		conn = psycopg2.connect(
			host="localhost",
			database="habrolinkdb",
			user="postgres",
			password="12345")
		startTime = time.time()			
		with conn.cursor() as cur:			
			if args.mode == "users":
				for i in range(args.index, len(usernames), args.count):
					try:
						user = get_user(usernames[i])
						if user != None:
								add_one_user(user, cur)
								conn.commit()
						else:
							print("\nskipped", user)	
					except Exception as e:
						cur.execute("ROLLBACK")
						conn.commit()
						print()
						print(e)
					currentTime = time.time()
					totalTime = (currentTime - startTime) * len(usernames) / (i + 0.1) / args.count
					ss = "\r User " + usernames[i] + " index " + str(i) + "/" + str(len(usernames)) + " time left " + str(totalTime - (currentTime - startTime)) + "s"
					if len(ss) < 80:
						ss += "*" * (80 - len(ss))
					print(ss, end="")
			else:
				for i in range(args.index, 1000000, args.count):				
					try:
						post = get_post(i)
						if post != None:
							with conn.cursor() as cur:			
								add_one_post(post, cur)	
								conn.commit()
						else:
							print("\nskipped", post)	
					except Exception as e:
						cur.execute("ROLLBACK")
						conn.commit()
						print()
						print(e)
					currentTime = time.time()
					totalTime = (currentTime - startTime) * 1000000 / (i + 0.1) / args.count
					ss = "\r Post " + str(i) + "/" + str(len(usernames)) + " time left " + str(totalTime - (currentTime - startTime)) + "s"
					if len(ss) < 80:
						ss += "*" * (80 - len(ss))
					print(ss, end="")
