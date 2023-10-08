# this is a module, which used for retrieving data from service
import requests
import json
import sys

def NoneFix(s):
	if s == None:
		return ""
	return s

# this function will collect info about user or return None
# returns - dict with user data
def get_user(uname : str):
	# main info
	cardRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/card?fl=ru&hl=ru")
	if cardRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/card?fl=ru&hl=ru")
		return None
	cardInfo = json.loads(cardRequest.text)

	# whois info
	whoisRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/whois?fl=ru&hl=ru")
	if whoisRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/whois?fl=ru&hl=ru")
		return None
	whoisInfo = json.loads(whoisRequest.text)

	# whois info
	occupationRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/occupation")
	if occupationRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/occupation")
		return None
	occupationInfo = json.loads(occupationRequest.text)

	# invited info
	invitedRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/invited?page=1")
	if invitedRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/invited?page=1")
		return None
	invitedPages = json.loads(invitedRequest.text)["pagesCount"]
	invitedInfo = []
	for i in range(1, invitedPages + 1):
		invitedRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/invited?page=" + str(i))
		if invitedRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/invited?page=" + str(i))
			return None
		invitedInfo += json.loads(invitedRequest.text)["userIds"]
	
	# hubs info
	hubsRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/subscriptions/hubs?page=1")
	if hubsRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/subscriptions/hubs?page=1")
		return None
	hubsPages = json.loads(hubsRequest.text)["pagesCount"]
	hubsInfo = []
	for i in range(1, hubsPages + 1):
		hubsRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/subscriptions/hubs?page=" + str(i))
		if hubsRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/subscriptions/hubs?page=" + str(i))
			return None
		hubsInfo += json.loads(hubsRequest.text)["hubIds"]
	
	# get list of posts id-s written by this user
	postRequest = requests.get("https://habr.com/kek/v2/articles/?user=" + uname + "&fl=ru&hl=ru&page=1&perPage=1")
	if postRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/articles/?user=" + uname + "&fl=ru&hl=ru&page=1&perPage=1")
		return None
	postsAmount = json.loads(postRequest.text)["pagesCount"]
	postsIndices = []
	postsPage = 1
	while (postsPage - 1) * 100 < postsAmount:
		postRequest = requests.get("https://habr.com/kek/v2/articles/?user=" + uname + "&fl=ru&hl=ru&page=" + str(postsPage) + "&perPage=100")
		if postRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/articles/?user=" + uname + "&fl=ru&hl=ru&page=" + str(postsPage) + "&perPage=100")
			return None
		postsIndices += list([int(t) for t in json.loads(postRequest.text)["articleIds"]])
		postsPage += 1
	
	# get list of comments written by this user
	# will do if needed, but not now	
	
	# get list of bookmarked posts id-s
	bookmarkRequest = requests.get("https://habr.com/kek/v2/articles/?user=" + uname + "&user_bookmarks=true&fl=ru&hl=ru&page=1&perPage=1")
	if bookmarkRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/articles/?user=" + uname + "&user_bookmarks=true&fl=ru&hl=ru&page=1&perPage=1")
		return None
	bookmarkAmount = json.loads(bookmarkRequest.text)["pagesCount"]
	bookmarkIndices = []
	bookmarkPage = 1
	while (bookmarkPage - 1) * 100 < bookmarkAmount:
		bookmarkRequest = requests.get("https://habr.com/kek/v2/articles/?user=" + uname + "&user_bookmarks=true&fl=ru&hl=ru&page=" + str(bookmarkPage) + "&perPage=100")
		if bookmarkRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/articles/?user=" + uname + "&user_bookmarks=true&fl=ru&hl=ru&page=" + str(bookmarkPage) + "&perPage=100")
			return None
		bookmarkIndices += list([int(t) for t in json.loads(bookmarkRequest.text)["articleIds"]])
		bookmarkPage += 1

	# get list of followers
	# hubs info
	followersRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/followers?page=1")
	if followersRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/followers?page=1")
		return None
	followersPages = json.loads(followersRequest.text)["pagesCount"]
	followersInfo = []
	for i in range(1, followersPages + 1):
		followersRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/followers?page=" + str(i))
		if followersRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/followers?page=" + str(i))
			return None
		followersInfo += json.loads(followersRequest.text)["authorIds"]

	# get list of followed (this user is a follower to them)
	followedRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/followed?page=1")
	if followedRequest.status_code != 200:
		print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/followed?page=1")
		return None
	followedPages = json.loads(followedRequest.text)["pagesCount"]
	followedInfo = []
	for i in range(1, followedPages + 1):
		followedRequest = requests.get("https://habr.com/kek/v2/users/" + uname + "/followed?page=" + str(i))
		if followedRequest.status_code != 200:
			print("Failed to retrieve", "https://habr.com/kek/v2/users/" + uname + "/followed?page=" + str(i))
			return None
		followedInfo += json.loads(followedRequest.text)["authorIds"]



	#combine all that data to one beautiful file
	userInfo = {}
	#copy data from card
	userInfo["id"] = NoneFix(cardInfo.get("alias", "")).lower() # str
	userInfo["fullname"] = NoneFix(cardInfo.get("fullname", "")) # str
	userInfo["avatar"] = NoneFix(cardInfo.get("avatarUrl", ""))  # url-str      
	userInfo["speciality"] = NoneFix(cardInfo.get("speciality", "")) # str
	userInfo["gender"] = int(cardInfo["gender"]) # str with number (1 for man as i understood)
	userInfo["rating"] = cardInfo["rating"] # number
	userInfo["karma"] = cardInfo["scoreStats"]["score"] # number
	userInfo["karma_votes_amount"] = cardInfo["scoreStats"]["votesCount"] # number
	userInfo["last_activity"] = NoneFix(cardInfo["lastActivityDateTime"]) # string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second
	userInfo["register"] = NoneFix(cardInfo["registerDateTime"]) # string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second
	userInfo["birthday"] = NoneFix(cardInfo.get("birthday", "")) # string in format YYYY-MM-DD, Y - year, M - mounth, D - day
	userInfo["is_readonly"] = cardInfo["isReadonly"] # bool 
	userInfo["invited"] = not cardInfo["canBeInvited"] # bool
	if cardInfo["location"] != None:
		if cardInfo["location"]["city"] != None:
			userInfo["location_city"] = NoneFix(cardInfo["location"]["city"]["title"])
		else:
			userInfo["location_city"] = ""

		if cardInfo["location"]["region"] != None:
			userInfo["location_region"] = NoneFix(cardInfo["location"]["region"]["title"])
		else:
			userInfo["location_region"] = ""

		if cardInfo["location"]["country"] != None:
			userInfo["location_country"] = NoneFix(cardInfo["location"]["country"]["title"])
		else:
			userInfo["location_country"] = ""
	else:
		userInfo["location_city"] = ""
		userInfo["location_region"] = ""
		userInfo["location_country"] = ""

	userInfo["workplace"] = [NoneFix(t.get("alias", "")) for t in cardInfo["workplace"]] # array of strings
	
	# copy data from whois	
	if whoisInfo["invitedBy"] != None:
		userInfo["invited_by"] = NoneFix(whoisInfo["invitedBy"].get("issuerLogin", "")).lower() # string
		userInfo["invited_at"] = NoneFix(whoisInfo["invitedBy"].get("timeCreated", "")) # string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second
	else:
		userInfo["invited_by"] = "" # string
		userInfo["invited_at"] = "" # string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second

	# copy data from occupation
	userInfo["salary"] = occupationInfo.get("salary", 0)  # number
	if occupationInfo["currency"] != None:
		userInfo["currency"] = occupationInfo["currency"]["id"] #string
	else:
		userInfo["currency"] = ""
	if occupationInfo["qualification"] != None:
		userInfo["qualification"] = occupationInfo["qualification"]["title"] #string
	else:
		userInfo["qualification"] = ""
	userInfo["specializations"] = [t["title"] for t in  occupationInfo["specializations"]]
	userInfo["skills"] = [t["name"] for t in  occupationInfo["skills"]]
	
	# copy data from invited
	userInfo["invites"] = [t.lower() for t in invitedInfo] # array with strings
 
	# copy data from hubs
	userInfo["hubs"] = hubsInfo # array with strings

	# copy data about posts
	userInfo["posts"] = postsIndices # array with numbers

	# copy data about bookmarks
	userInfo["bookmarks"] = bookmarkIndices # array with numbers
	
	# copy data about followers
	userInfo["followers"] = [t.lower() for t in followersInfo] # array with str

	# copy data about followed
	userInfo["followed"] = [t.lower() for t in followedInfo] # array with str

	return userInfo

	
	
# this function will collect info about post or return None
# returns - dict with post data
def get_post(index : int):	
	postRequest = requests.get("https://habr.com/kek/v2/articles/" + str(index) + "/?fl=ru&hl=ru")
	if postRequest.status_code != 200:
		print("\nFailed to retrieve", "https://habr.com/kek/v2/articles/" + str(index) + "/?fl=ru&hl=ru")
		return None
	postInfo = json.loads(postRequest.text)

	ourPostInfo = {}
	ourPostInfo["id"] = int(postInfo["id"]) # number
	ourPostInfo["time"] = postInfo["timePublished"] # string in format YYYY-MM-DDThh:mm:ss+00:00, Y - year, M - mounth, D - day, h - hour, m - minute, s - second
	ourPostInfo["is_corp"] = postInfo["isCorporative"]  # bool
	ourPostInfo["lang"] = postInfo["lang"] # string 
	ourPostInfo["title"] = postInfo["titleHtml"] # string 
	ourPostInfo["type"] = postInfo["postType"] # string 
	ourPostInfo["author"] = postInfo["author"]["alias"] # string 
	ourPostInfo["comments_count"] = int(postInfo["statistics"]["commentsCount"]) # number
	ourPostInfo["favorites_count"] = int(postInfo["statistics"]["favoritesCount"]) # number
	ourPostInfo["reading_count"] = int(postInfo["statistics"]["readingCount"]) # number
	ourPostInfo["score"] = int(postInfo["statistics"]["score"]) # number
	ourPostInfo["votes_up"] = int(postInfo["statistics"]["votesCountPlus"]) # number
	ourPostInfo["votes_down"] = int(postInfo["statistics"]["votesCountMinus"]) # number
	ourPostInfo["votes_count"] = int(postInfo["statistics"]["votesCount"]) # number 
	ourPostInfo["hubs"] = [ t["alias"] for t in postInfo["hubs"]] # array with strings
	ourPostInfo["tags"] = [ t["titleHtml"] for t in postInfo["tags"]] # array with strings
	if postInfo["readingTime"] == None:
		ourPostInfo["reading_minutes"] = 0                            # fake number
	else:
		ourPostInfo["reading_minutes"] = int(postInfo["readingTime"]) # number
	#ourPostInfo["content"] = postInfo["textHtml"] # string 

	commentsRequest = requests.get("https://habr.com/kek/v2/articles/" + str(index) + "/comments?fl=ru&hl=ru")
	if commentsRequest.status_code != 200:
		print("\nFailed to retrieve comments for", "https://habr.com/kek/v2/articles/" + str(index) + "/comments?fl=ru&hl=ru")
		ourPostInfo["comments"] = []		
	else:
		commentsInfo = json.loads(commentsRequest.text)
		comments = []
		for comment_id in commentsInfo["comments"]:
			if not bool(commentsInfo["comments"][comment_id]["author"]):
				continue
			comment = {}
			comment["id"] = int(commentsInfo["comments"][comment_id]["id"]) # number
			if commentsInfo["comments"][comment_id]["parentId"] == None:
				comment["parent_id"] = -1
			else:
				comment["parent_id"] = int(commentsInfo["comments"][comment_id]["parentId"]) # number
			comment["post_id"] = index # number
			comment["user_id"] = commentsInfo["comments"][comment_id]["author"]["alias"] # string
			comment["time"] = commentsInfo["comments"][comment_id]["timePublished"] # string
			#comment["content"] =  commentsInfo["comments"][comment_id]["textHtml"]
			comment["score"] = int(commentsInfo["comments"][comment_id]["score"]) # number
			comment["votes_count"] = int(commentsInfo["comments"][comment_id]["votesCount"]) # number			
			comments.append(comment)
		ourPostInfo["comments"] = comments						
	return ourPostInfo

if __name__ == "__main__":
	# test requests
	#print(get_user("sairsey"))
	print(get_post(1))
	print(get_post(2))
	print(get_post(3))
	print(get_post(200))
	print(get_post(326852))
