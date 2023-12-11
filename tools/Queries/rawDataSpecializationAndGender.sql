SELECT  
    "userToSpecialization".specialization_id,
	"users".gender,
	count("userToSpecialization".id)
FROM 
    public."userToSpecialization" 
JOIN
    public."users" 
ON
    "userToSpecialization".user_id = "users".id
GROUP BY
	("userToSpecialization".specialization_id, "users".gender)
ORDER BY
	("userToSpecialization".specialization_id, "users".gender)
;