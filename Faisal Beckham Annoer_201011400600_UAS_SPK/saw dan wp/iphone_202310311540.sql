--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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
-- Name: iphone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.iphone (
    brand text,
    ram text,
    battery text,
    processor text,
    kamera text,
    harga bigint
);


ALTER TABLE public.iphone OWNER TO postgres;

--
-- Data for Name: iphone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.iphone (brand, ram, battery, processor, kamera, harga) FROM stdin;
APPLE IPHONE 6S PLUS	2 GB	2915 mAh	APPLE A8	8 MP(BELAKANG) & 1.2 MP(DEPAN)	8000000
APPLE IPHONE 7 PLUS	3 GB	2900 mAh	APPLE A10 FUSION	24 MP(BELAKANG) & 7 MP(DEPAN)	10000000
APPLE IPHONE 8 PLUS	3 GB	2691 mAh	APPLE A11 BIONIC	24 MP(BELAKANG) & 7 MP(DEPAN)	11000000
APPLE IPHONE XR	3 GB	2716 mAh	APPLE A11 BIONIC	12 MP(BELAKANG) & 7 MP(DEPAN)	15000000
APPLE IPHONE 11 PRO MAX	4 GB	3969 mAh	APPLE A13 BIONIC	12+12+12 MP(BELAKANG) & 12 MP(DEPAN)	18000000
APPLE IPHONE 12 MINI	4 GB	2227 mAh	APPLE A14 BIONIC	12 MP(BELAKANG) & 12 MP(DEPAN)	13000000
APPLE IPHONE 12 PRO MAX	6 GB	3687 mAh	APPLE A14 BIONIC	12+12+12 MP(BELAKANG) & 12 MP(DEPAN)	18000000
APPLE IPHONE 13 PRO MAX	6 GB	4352 mAh	APPLE A15 BIONIC	48+12+12 MP(BELAKANG) & 12 MP(DEPAN)	18000000
APPLE IPHONE 14 PRO MAX	6 GB	4422 mAh	APPLE A16 BIONIC	48+12+12 MP(BELAKANG) & 12 MP(DEPAN)	19000000
APPLE IPHONE 15 PRO MAX	8 GB	4422 mAh	APPLE A17 BIONIC	48+12+12 MP(BELAKANG) & 12 MP(DEPAN)	20000000
\.


--
-- PostgreSQL database dump complete
--

