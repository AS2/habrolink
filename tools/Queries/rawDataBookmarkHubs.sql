SELECT 
	"userToBookmark".user_id,
    "postToHub".hub_id 
FROM 
    public."postToHub" 
JOIN
	public."userToBookmark"
ON
	"postToHub".post_id = "userToBookmark".post_id
ORDER BY user_id;