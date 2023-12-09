SELECT
	COALESCE(res.sal::varchar(255),'total') AS field,
	sum(res.count)
FROM (
	select 
		count(users.id), 
		COALESCE(users.salary, 0) AS sal
	FROM 
		users 
	where 
		location_country <> '' 
		and location_region <> '' 
		and location_city <> ''
		and speciality <> '' 
	GROUP BY (sal)
	ORDER BY (count) DESC
) res
GROUP BY ROLLUP(res.sal)
;