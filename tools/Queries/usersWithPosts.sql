SELECT author as user_id FROM public."posts" GROUP BY (user_id) ORDER BY user_id