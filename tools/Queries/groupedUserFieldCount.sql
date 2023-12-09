SELECT
	COALESCE(res.location_country,'total') AS field,
	sum(res.count)
FROM (
	select 
		count(users.id), 
		users.location_country 
	FROM 
		users 
	where 
		location_country <> '' 
		and location_region <> '' 
		and location_city <> ''
		and speciality <> '' 
	GROUP BY (location_country)
	ORDER BY (count) DESC
) res
GROUP BY ROLLUP(res.location_country)
;