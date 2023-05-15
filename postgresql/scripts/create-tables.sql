DROP TABLE IF EXISTS garden CASCADE;
DROP TABLE IF EXISTS vegetable CASCADE;
DROP TABLE IF EXISTS vegetable_price CASCADE;
DROP TABLE IF EXISTS vegetable_on_discount CASCADE;
DROP TABLE IF EXISTS beef CASCADE;
DROP TABLE IF EXISTS beef_part CASCADE;
DROP TABLE IF EXISTS beef_part_price CASCADE;
DROP TABLE IF EXISTS beef_part_on_discount CASCADE;
DROP TABLE IF EXISTS chicken CASCADE;
DROP TABLE IF EXISTS chicken_price CASCADE;
DROP TABLE IF EXISTS chicken_on_discount CASCADE;
DROP TABLE IF EXISTS juice CASCADE;
DROP TABLE IF EXISTS juice_price CASCADE;
DROP TABLE IF EXISTS juice_on_discount CASCADE;
DROP TYPE IF EXISTS wine_color CASCADE;
DROP TABLE IF EXISTS wine CASCADE;
DROP TABLE IF EXISTS wine_price CASCADE;
DROP TABLE IF EXISTS wine_on_discount CASCADE;


CREATE TABLE garden (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    gps_position POINT
);

CREATE TABLE vegetable (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE vegetable_price(
    id SERIAL PRIMARY KEY,
    garden_id INT REFERENCES garden(id) ON DELETE NO ACTION,
    vegetable_id INT REFERENCES vegetable(id) ON DELETE NO ACTION,
    price FLOAT
);

CREATE TABLE vegetable_on_discount(
    vegetable_price_id INT REFERENCES vegetable_price(id) ON DELETE NO ACTION,
    discount FLOAT,
    valid_until DATE
);

CREATE TABLE beef (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE beef_part(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE beef_part_price(
    id SERIAL PRIMARY KEY,
    garden_id INT REFERENCES garden(id) ON DELETE NO ACTION,
    beef_id INT REFERENCES beef(id) ON DELETE NO ACTION,
    beef_part_id INT REFERENCES beef_part(id) ON DELETE NO ACTION,
    price FLOAT
);

CREATE TABLE beef_part_on_discount(
    beef_part_price_id INT REFERENCES beef_part_price(id) ON DELETE NO ACTION,
    discount FLOAT,
    valid_until DATE
);

CREATE TABLE chicken (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE chicken_price(
    id SERIAL PRIMARY KEY,
    garden_id INT REFERENCES garden(id) ON DELETE NO ACTION,
    chicken_id INT REFERENCES chicken(id) ON DELETE NO ACTION,
    price FLOAT
);

CREATE TABLE chicken_on_discount(
    chicken_price_id INT REFERENCES chicken_price(id) ON DELETE NO ACTION,
    discount FLOAT,
    valid_until DATE
);

CREATE TABLE juice (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE juice_price(
    id SERIAL PRIMARY KEY,
    garden_id INT REFERENCES garden(id) ON DELETE NO ACTION,
    juice_id INT REFERENCES juice(id) ON DELETE NO ACTION,
    price FLOAT
);

CREATE TABLE juice_on_discount(
    juice_price_id INT REFERENCES juice_price(id) ON DELETE NO ACTION,
    discount FLOAT,
    valid_until DATE
);

CREATE TYPE wine_color AS ENUM ('Ambré','Blanc', 'Gris', 'Grenat','Rancio', 'Rouge', 'Rosé', 'Tuilé');

CREATE TABLE wine (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    color wine_color NOT NULL
);

CREATE TABLE wine_price(
    id SERIAL PRIMARY KEY,
    garden_id INT REFERENCES garden(id) ON DELETE NO ACTION,
    wine_id INT REFERENCES wine(id) ON DELETE NO ACTION,
    price FLOAT
);

CREATE TABLE wine_on_discount(
    wine_price_id INT REFERENCES wine_price(id) ON DELETE NO ACTION,
    discount FLOAT,
    valid_until DATE
);
