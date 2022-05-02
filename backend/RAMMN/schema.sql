-- Create tables should they not exist
-- users, privileges, interests, user_interests, and search history

-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    r_identity character varying(255) COLLATE pg_catalog."default" NOT NULL,
    r_username character varying(35) COLLATE pg_catalog."default" NOT NULL,
    last_accessed timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT unique_r_identity UNIQUE (r_identity)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to lcnocbrmucvymo;

-- Table: public.privileges

-- DROP TABLE IF EXISTS public.privileges;

CREATE TABLE IF NOT EXISTS public.privileges
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    level numeric(1,0) NOT NULL DEFAULT 9,
    CONSTRAINT privileges_pkey PRIMARY KEY (user_id),
    CONSTRAINT privileges_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.privileges
    OWNER to lcnocbrmucvymo;

-- Trigger: set_default_user_privilege

-- DROP TRIGGER IF EXISTS set_default_user_privilege ON public.users;

CREATE TRIGGER set_default_user_privilege
    AFTER INSERT
    ON public.users
    FOR EACH ROW
    EXECUTE FUNCTION public.set_default_user_privilege();

-- Table: public.interests

-- DROP TABLE IF EXISTS public.interests;

CREATE TABLE IF NOT EXISTS public.interests
(
    id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    interest character varying(255) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    CONSTRAINT interests_pkey PRIMARY KEY (id),
    CONSTRAINT interests_interest_key UNIQUE (interest)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.interests
    OWNER to lcnocbrmucvymo;

-- Table: public.users_interests

-- DROP TABLE IF EXISTS public.users_interests;

CREATE TABLE IF NOT EXISTS public.users_interests
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    interest_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    date_added date NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT users_interests_interest_id_fkey FOREIGN KEY (interest_id)
        REFERENCES public.interests (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT users_interests_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users_interests
    OWNER to lcnocbrmucvymo;

-- Table: public.search_history

-- DROP TABLE IF EXISTS public.search_history;

CREATE TABLE IF NOT EXISTS public.search_history
(
    user_id character varying(10) COLLATE pg_catalog."default",
    search text COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT search_history_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE SET NULL
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.search_history
    OWNER to lcnocbrmucvymo;

