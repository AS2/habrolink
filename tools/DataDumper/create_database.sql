--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2023-09-15 19:15:44

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 236 (class 1259 OID 16492)
-- Name: postToHub; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."postToHub" (
    id bigint NOT NULL,
    post_id bigint,
    hub_id text
);


ALTER TABLE public."postToHub" OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 16491)
-- Name: postToHub_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."postToHub" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."postToHub_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 234 (class 1259 OID 16484)
-- Name: postToTag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."postToTag" (
    id bigint NOT NULL,
    post_id bigint,
    tag text
);


ALTER TABLE public."postToTag" OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 16483)
-- Name: postToTags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."postToTag" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."postToTags_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 232 (class 1259 OID 16476)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id bigint NOT NULL,
    creation_time timestamp with time zone,
    is_corp boolean,
    lang text,
    title text,
    type text,
    author text,
    comments_count integer,
    favorites_count integer,
    reading_count integer,
    score integer,
    votes_up integer,
    votes_down integer,
    votes_count integer,
    reading_minutes integer
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16459)
-- Name: userToBookmark; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToBookmark" (
    id bigint NOT NULL,
    user_id text,
    post_id integer
);


ALTER TABLE public."userToBookmark" OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16464)
-- Name: userToBookmark_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToBookmark" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToBookmark_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 231 (class 1259 OID 16468)
-- Name: userToFollow; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToFollow" (
    id bigint NOT NULL,
    parent_id text,
    follower_id text
);


ALTER TABLE public."userToFollow" OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16467)
-- Name: userToFollower_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToFollow" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToFollower_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 225 (class 1259 OID 16444)
-- Name: userToHub; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToHub" (
    id bigint NOT NULL,
    user_id text,
    hub_id text
);


ALTER TABLE public."userToHub" OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16443)
-- Name: userToHub_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToHub" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToHub_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 223 (class 1259 OID 16436)
-- Name: userToInvite; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToInvite" (
    id bigint NOT NULL,
    parent_id text,
    child_id text
);


ALTER TABLE public."userToInvite" OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16435)
-- Name: userToInvites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToInvite" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToInvites_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 227 (class 1259 OID 16452)
-- Name: userToPost; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToPost" (
    id bigint NOT NULL,
    user_id text,
    post_id integer
);


ALTER TABLE public."userToPost" OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16451)
-- Name: userToPost_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToPost" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToPost_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 16428)
-- Name: userToSkill; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToSkill" (
    id bigint NOT NULL,
    user_id text,
    skill_id text
);


ALTER TABLE public."userToSkill" OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16427)
-- Name: userToSkill_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToSkill" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToSkill_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 219 (class 1259 OID 16420)
-- Name: userToSpecialization; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToSpecialization" (
    id bigint NOT NULL,
    user_id text,
    specialization_id text
);


ALTER TABLE public."userToSpecialization" OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16419)
-- Name: userToSpecialization_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToSpecialization" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToSpecialization_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 16412)
-- Name: userToWorkplace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."userToWorkplace" (
    id bigint NOT NULL,
    user_id text,
    workplace_id text
);


ALTER TABLE public."userToWorkplace" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16411)
-- Name: userToWorkplace_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."userToWorkplace" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."userToWorkplace_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 16399)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id text NOT NULL,
    fullname text,
    avatar text,
    speciality text,
    gender integer,
    rating real,
    karma real,
    karma_votes_amount integer,
    last_activity timestamp with time zone,
    register timestamp with time zone,
    birthday date,
    is_readonly boolean,
    invited boolean,
    location_city text,
    location_region text,
    location_country text,
    invited_by text,
    invited_at timestamp with time zone,
    salary integer,
    currency text,
    qualification text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 4710 (class 2606 OID 16498)
-- Name: postToHub postToHub_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."postToHub"
    ADD CONSTRAINT "postToHub_pkey" PRIMARY KEY (id);


--
-- TOC entry 4708 (class 2606 OID 16490)
-- Name: postToTag postToTags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."postToTag"
    ADD CONSTRAINT "postToTags_pkey" PRIMARY KEY (id);


--
-- TOC entry 4706 (class 2606 OID 16482)
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- TOC entry 4702 (class 2606 OID 16466)
-- Name: userToBookmark userToBookmark_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToBookmark"
    ADD CONSTRAINT "userToBookmark_pkey" PRIMARY KEY (id);


--
-- TOC entry 4704 (class 2606 OID 16474)
-- Name: userToFollow userToFollower_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToFollow"
    ADD CONSTRAINT "userToFollower_pkey" PRIMARY KEY (id);


--
-- TOC entry 4698 (class 2606 OID 16450)
-- Name: userToHub userToHub_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToHub"
    ADD CONSTRAINT "userToHub_pkey" PRIMARY KEY (id);


--
-- TOC entry 4696 (class 2606 OID 16442)
-- Name: userToInvite userToInvites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToInvite"
    ADD CONSTRAINT "userToInvites_pkey" PRIMARY KEY (id);


--
-- TOC entry 4700 (class 2606 OID 16458)
-- Name: userToPost userToPost_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToPost"
    ADD CONSTRAINT "userToPost_pkey" PRIMARY KEY (id);


--
-- TOC entry 4694 (class 2606 OID 16434)
-- Name: userToSkill userToSkill_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToSkill"
    ADD CONSTRAINT "userToSkill_pkey" PRIMARY KEY (id);


--
-- TOC entry 4692 (class 2606 OID 16426)
-- Name: userToSpecialization userToSpecialization_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToSpecialization"
    ADD CONSTRAINT "userToSpecialization_pkey" PRIMARY KEY (id);


--
-- TOC entry 4690 (class 2606 OID 16418)
-- Name: userToWorkplace userToWorkplace_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."userToWorkplace"
    ADD CONSTRAINT "userToWorkplace_pkey" PRIMARY KEY (id);


--
-- TOC entry 4688 (class 2606 OID 16410)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


-- Completed on 2023-09-15 19:15:45
--
-- PostgreSQL database dump complete
--

