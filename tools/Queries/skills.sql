SELECT  
    "userToSkill".skill_id,
	count("userToSkill".id)
FROM 
    public."userToSkill"
GROUP BY
	("userToSkill".skill_id)
ORDER BY
	(count) DESC
;