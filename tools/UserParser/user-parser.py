# this is a tool, for retrieving user list
import requests
import json
import string
import itertools
import os
import os.path
import time
import sys

# this function will find all users in search with specific prefix
# Argument - prefix to check
# returns - list with usernames
def users_by_search(prefix : str):
	userNames = []
	for i in range(1, 51):	
		r = requests.get("https://habr.com/kek/v2/users/search?q=" + prefix + "&target_type=users&page=" + str(i))
		if r.status_code != 200:
			break
		data = json.loads(r.text)
		for username in data["userIds"]:
			username = username.lower()
			#if username.startswith(prefix):
			userNames.append(username)
	return userNames

# this function will find all users in search with specific prefix
# Argument - length of prefixes and start prefix
# returns - list with prefixes
def build_prefixes(prefixLength : int, skipUntill = ""):
	prefixes = [] # list of all prefixes
	chars = string.ascii_lowercase + string.digits
	skip = (skipUntill != "")
	for item in itertools.product(chars, repeat=prefixLength):
		if "".join(item) == skipUntill:
			skip = False
		if skip:
			continue
		prefixes.append("".join(item))
	return prefixes


# this function will return all already dumped users
# Argument - length of prefixes and start prefix
# returns - list with prefixes
def fill_known_users(prefixLength : int):
	knownUsers = set()
	# create directory
	if not os.path.isdir("tmp"):
		os.mkdir("tmp")
	# check 
	if os.path.isfile("tmp/users" + str(prefixLength) + ".txt"):
		with open("tmp/users" + str(prefixLength) + ".txt", "r") as f:
			keys = f.read().split("\n")
			for key in keys:
				knownUsers.add(key)
	return knownUsers
	

# this function will dump to file all users in found in search all possible prefix-es with given length 
# Argument - length
def find_all_users(prefixLength : int, skipUntill = ""):
	 # map with users for storing only unique
	print("Start building prefixes with length", prefixLength)
	prefixes = build_prefixes(prefixLength, skipUntill)
	print("Finished building prefixes")	

	print("Check already known users...")
	knownUsers = fill_known_users(prefixLength)

	print("Start parse.")

	f = open("tmp/users" + str(prefixLength) + ".txt", "a")
	startTime = time.time()
	for i in range(len(prefixes)):		
		result = []

		repeat = True
		while repeat:
			repeat = False
			try:
				result = users_by_search(prefixes[i])
			except:
				currentTime = time.time()
				totalTime = (currentTime - startTime) * len(prefixes) / (i + 0.1)
				print("\rPrefix: '" + prefixes[i] + "' Size:", len(knownUsers), "Progress:", i, "/", len(prefixes), "Seconds left:", totalTime - (currentTime - startTime), "(crushed but we are trying)", end="")
				repeat = True

		currentTime = time.time()
		totalTime = (currentTime - startTime) * len(prefixes) / (i + 0.1)
		print("\rPrefix: '" + prefixes[i] + "' Size:", len(knownUsers), "Progress:", i, "/", len(prefixes), "Seconds left:", totalTime - (currentTime - startTime), end="")
		for user in result:
			if not (user in knownUsers):
				knownUsers.add(user)
				f.write(user + "\n")
		if i % 100 == 0:
			f.close()
			f = open("tmp/users" + str(prefixLength) + ".txt", "a")
	f.close()						

if __name__ == "__main__":
	prefixLength = 2
	skipUntill = ""
	if len(sys.argv) > 2:
		prefixLength = int(sys.argv[1])
	else:
		print("Set prefix length to 2 by default")
	
	if len(sys.argv) > 3:
		skipUntill = sys.argv[2]
		print("Will skip all prefixes before '" + skipUntill + "'")
	try:
		find_all_users(prefixLength, skipUntill)
	except:
		print("\nexception occured. Please remember prefix, fix bat file and restart.")
		input()