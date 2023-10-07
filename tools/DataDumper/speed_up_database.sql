ALTER TABLE public."userToBookmark" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToBookmark" ADD FOREIGN KEY ("post_id") REFERENCES public."posts" ("id");

ALTER TABLE public."postToTag" ADD FOREIGN KEY ("post_id") REFERENCES public."posts" ("id");

ALTER TABLE public."userToFollow" ADD FOREIGN KEY ("parent_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToFollow" ADD FOREIGN KEY ("follower_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToSkill" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToInvite" ADD FOREIGN KEY ("parent_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToInvite" ADD FOREIGN KEY ("child_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToHub" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToSpecialization" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToPost" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."userToPost" ADD FOREIGN KEY ("post_id") REFERENCES public."posts" ("id");

ALTER TABLE public."userToWorkplace" ADD FOREIGN KEY ("user_id") REFERENCES public."users" ("id");

ALTER TABLE public."postToHub" ADD FOREIGN KEY ("post_id") REFERENCES public."posts" ("id");
