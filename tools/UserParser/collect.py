# this is a tool, for retrieving user list
import os

# this function will collect usernames from files, dumped by user-parser.py
# returns - set with usernames
def collect_usernames():
	allNames = set()
	for filename in os.listdir("tmp"):
		if filename.startswith("user") and filename.endswith(".txt"):
			path = os.path.join("tmp", filename)
			if os.path.isfile(path):	
				with open(path, "rt") as f:
					unames= f.read().split('\n')
					for username in unames:
						allNames.add(username)
	allNames.discard("")
	return allNames
	
			

if __name__ == "__main__":
	names = list(collect_usernames())
	names.sort()	
	with open("users.txt", "wt") as f:
		for name in names:
			f.write(name + "\n")