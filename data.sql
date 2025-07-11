--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: operations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operations (
    strategy character varying(30),
    ticker character varying(30),
    side character varying(5),
    quantity numeric(15,8),
    price numeric(15,8),
    type character varying(15),
    commission numeric(15,8),
    fee numeric(15,8),
    binance_operation_id bigint,
    operation_id integer NOT NULL,
    epoch bigint,
    pnl numeric(15,6),
    epoch_fee bigint
);


ALTER TABLE public.operations OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

