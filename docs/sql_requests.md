# SQL requests
В данном файле описаны примеры SQL запросов используемые в данном проекте.

## Get Person_id for user
Arguments:
  - user_id Индекс пользователя информацию о котором мы хотим узнать
```sql
  SELECT "user"."person_id" FROM "user" WHERE "user"."user_id" == {user_id};
```
## Get user_id for person
Arguments:
  - person_id Индекс человека, информацию о котором мы хотим узнать
```sql
  SELECT "user"."user_id" FROM "user" WHERE "user"."person_id" == {person_id};
```
## Get user password hash
  - user_id Индекс пользователя, информацию о котором мы хотим узнать
```sql
  SELECT "user"."password_hash" FROM "user" WHERE "user"."user_id" == {user_id};
```
## Get person full info
  - person_id Индекс человека, информацию о котором мы хотим узнать
```sql
  SELECT * FROM "person" WHERE "person"."id" == {person_id};
  SELECT "personToSkill"."skill" FROM "personToSkill" WHERE "personToSkill"."person_id" == {person_id};
  SELECT "personToSpeciality"."speciality" FROM "personToSpeciality" WHERE "personToSpeciality"."person_id" == {person_id};
  SELECT ("habr_link", "login") FROM "users" WERE "users"."person_id" == {person_id}; 
```
## Get person short info
  - person_id Индекс человека, информацию о котором мы хотим узнать
```sql
  SELECT ("id", "fullname", "avatar", "source", "habr_karma", "habr_rating") FROM "person" WHERE "person"."id" == {person_id};
  SELECT ("habr_link", "login") FROM "users" WERE "users"."person_id" == {person_id}; 
```
## Create new, non Habr user
  - login Логин пользователя (почта)
  - password_hash Хеш от пароля
  - fullname Полное имя
  - avatar Аватар
  - gender Пол
  - birthday Дата рождения
  - location_country Страна проживания
  - location_city Город проживания
  - location_region Регион проживания
  - salary Ожидаемая заработная плата
```sql
  INSERT INTO "person" ("id", "source", "fullname", "avatar", "gender", "birthday", "location_country", "location_city", "location_region", "salary", "habr_karma", "habr_rating")
    VALUES ('habrolinker-'+{login}, 1, {fullname}, {avatar}, {gender}, {birthday}, {location_country}, {location_city}, {location_region}, {salary}, 0, 0);
  INSERT INTO "user" ("login", "password_hash", "person_id") VALUES ({login}, {password_hash}, 'habrolinker-'+{login});
```
## Create new, Habr user
  - login Логин пользователя (почта)
  - password_hash Хеш от пароля
  - person_id пользоваль из хабр.
```sql
  INSERT INTO "user" ("login", "password_hash", "person_id") VALUES ({login}, {password_hash}, {person_id});
  UPDATE "person" SET "source" = 0 WHERE "person"."id" = person_id;
```
## Add Skill to User
  - person_id Индекс человека
  - skill Название умения
```sql
  INSERT INTO "personToSkill" ("person_id", "skill") VALUES ({person_id}, {skill});
```
## Add Speciality to User
  - person_id Индекс человека
  - speciality Название умения
```sql
  INSERT INTO "personToSpeciality" ("person_id", "speciality") VALUES ({person_id}, {speciality});
```
## Send message
  - from Индекс отправителя
  - to Индекс получателя
  - message текст сообщения
```sql
  INSERT INTO "message" ("from", "to", "message") VALUES ({from}, {to}, {message});
```
## Get all messages in chat
  - person1 Индекс первого пользователя
  - person2 Индекс второго пользователя
```sql
  SELECT * FROM "message" WHERE ("message"."from" = {person1} AND "message"."to" = {person2}) OR ("message"."from" = {person2} AND "message"."to" = {person1});
```
## Get all chats
  - user_id Индекс пользователя
```sql
SELECT DISTINCT "chats"."user_id" FROM (
      (SELECT DISTINCT "message"."from" AS "user_id" FROM "message" WHERE "message"."to" = {user_id})
      UNION 
      (SELECT DISTINCT "message"."to" AS "user_id" FROM "message" WHERE "message"."from" = {user_id})
) AS "chats";
```
## Search for users
  - source - Где искать человека. 0 - отовсюду, 2 - только Хабр, 1 - только Хабролинкере. По умолчанию 0.
  - habr_rating_low нижний порог рейтинга в Хабр
  - habr_rating_high верхний порог рейтинга в Хабр
  - habr_karma_low нижний порог кармы в Хабр
  - habr_karma_high верхний порог кармы в Хабр
  - age_low нижний порог возразста
  - age_high верхний порог возразста
  - location_country Страна проживания
  - location_city Город проживания
  - location_region Регион проживания
  - salary_low нижний порог зп
  - salary_high верхний порог зп
  - skill\[i\] массив скиллов
  - speciality \[i\] массив скиллов
```sql
WITH "skills" AS (
  SELECT "person_id" FROM "personToSkill" WHERE "personToSkill"."skill" = {skill[i]}
), "speciality" AS (
  SELECT "person_id" FROM "personToSpeciality" WHERE "personToSpeciality"."speciality" = {skill[i]}
)
SELECT "id" FROM "person" JOIN "skills" ON "skills"."person_id" = "person"."id" JOIN "speciality" ON "speciality"."person_id" = "person"."id" WHERE
  ("person"."source" = 0 OR "person"."source" = {source}) AND
  ("person"."habr_rating" = 0 OR ("person"."habr_rating" >= {habr_rating_low} AND "person"."habr_rating" <= {habr_rating_high})) AND
  ( date_part('year',age("person"."birthday")) >= {age_low} AND date_part('year',age("person"."birthday")) <= {age_high}) AND
  ({location_country} = '' OR "person"."location_country" = '' OR "person"."location_country" = {location_country}) AND
  ({location_city} = '' OR "person"."location_city" = '' OR "person"."location_city" = {location_city}) AND
  ({location_region} = '' OR "person"."location_region" = '' OR "person"."location_region" = {location_region}) AND
  ("person"."salary" = 0 OR ("person"."salary" >= {salary_low} AND "person"."salary" <= {salary_high})) GROUP BY "id";
```
## Mark person
  - user_id индекс пользователя, который отмечает
  - person_id индекс человека которого отмечают
```sql
INSERT INTO "marked" ("user_id", "person_id") VALUES ({user_id}, {person_id}) ON CONFLICT DO NOTHING;
```
## Unmark user

## Mark person
  - user_id индекс пользователя, который снимает отметку
  - person_id индекс человека с которого снимают отметку
```sql
DELETE FROM "marked" WHERE "user_id" = {user_id} AND "person_id" = {person_id};
```
## Get all marked users
  - user_id индекс пользователя, который смотрит отметки
```sql
SELECT "person_id" FROM "marked" WHERE "user_id" = {user_id};
```
