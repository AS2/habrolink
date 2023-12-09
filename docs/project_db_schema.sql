CREATE TABLE "person" (
  "id" text PRIMARY KEY ,
  "source" integer,
  "fullname" text,
  "avatar" text,
  "gender" integer,
  "birthday" date,
  "location_country" text,
  "location_city" text,
  "location_region" text,
  "salary" integer,
  "habr_karma" integer,
  "habr_rating" integer
);

CREATE TABLE "personToSkill" (
  "id" SERIAL PRIMARY KEY,
  "person_id" text REFERENCES "person" ("id"),
  "skill" text
);

CREATE TABLE "personToSpeciality" (
  "id" SERIAL PRIMARY KEY,
  "person_id" text REFERENCES "person" ("id"),
  "speciality" text
);

CREATE TABLE "user" (
  "id" SERIAL PRIMARY KEY,
  "login" text,
  "password_hash" text,
  "person_id" text REFERENCES "person" ("id")
);

CREATE TABLE "marked" (
  "id" SERIAL PRIMARY KEY,
  "user_id" integer REFERENCES "user" ("id"),
  "person_id" text REFERENCES "person" ("id")
);

CREATE TABLE "message" (
  "id" SERIAL PRIMARY KEY,
  "from" integer REFERENCES "user" ("id"),
  "to" integer REFERENCES "user" ("id"),
  "message" text
);