-- Create tables should they not exist
-- users, privileges, interests, user_interests, and search history

-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    sub character varying(255) COLLATE pg_catalog."default" NOT NULL,
    fname character varying(35) COLLATE pg_catalog."default" NOT NULL,
    lname character varying(35) COLLATE pg_catalog."default" NOT NULL,
    gender numeric(1,0) NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    birthday date NOT NULL,
    last_accessed timestamp without time zone NOT NULL DEFAULT now(),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT unique_email UNIQUE (email),
    CONSTRAINT unique_sub UNIQUE (sub),
    CONSTRAINT gender_code CHECK (gender = ANY (ARRAY[0::numeric, 1::numeric, 2::numeric, 9::numeric]))
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to lcnocbrmucvymo;

COMMENT ON CONSTRAINT gender_code ON public.users
    IS 'Per ISO/IEC 5218 standards, 0: Not known, 1: Male, 2: Female, 9: Not applicable';

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

