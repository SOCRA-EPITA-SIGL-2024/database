-- Database: socarotte

DROP DATABASE IF EXISTS socarotte;

CREATE DATABASE socarotte
    WITH
    OWNER = sigl2024
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE socarotte
    IS 'Database for socarotte';