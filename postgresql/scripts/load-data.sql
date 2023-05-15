COPY garden(id,title,gps_position)
FROM '/tmp/scripts/data/garden.csv' WITH DELIMITER ';' CSV HEADER;

COPY vegetable(id,name)
FROM '/tmp/scripts/data/vegetable.csv' DELIMITER ';' CSV HEADER;
COPY vegetable_price(id,garden_id,vegetable_id,price)
FROM '/tmp/scripts/data/vegetable_price.csv' DELIMITER ';' CSV HEADER;
COPY vegetable_on_discount(vegetable_price_id,discount,valid_until)
FROM '/tmp/scripts/data/vegetable_on_discount.csv' DELIMITER ';' CSV HEADER;

COPY beef(id,name)
FROM '/tmp/scripts/data/beef.csv' DELIMITER ';' CSV HEADER;
COPY beef_part(id,name)
FROM '/tmp/scripts/data/beef_part.csv' DELIMITER ';' CSV HEADER;
COPY beef_part_price(id,garden_id,beef_id,beef_part_id,price)
FROM '/tmp/scripts/data/beef_part_price.csv' DELIMITER ';' CSV HEADER;
COPY beef_part_on_discount(beef_part_price_id,discount,valid_until)
FROM '/tmp/scripts/data/beef_part_on_discount.csv' DELIMITER ';' CSV HEADER;

COPY chicken(id,name,description)
FROM '/tmp/scripts/data/chicken.csv' DELIMITER ';' CSV HEADER;
COPY chicken_price(id,garden_id,chicken_id,price)
FROM '/tmp/scripts/data/chicken_price.csv' DELIMITER ';' CSV HEADER;
COPY chicken_on_discount(chicken_price_id,discount,valid_until)
FROM '/tmp/scripts/data/chicken_on_discount.csv' DELIMITER ';' CSV HEADER;

COPY wine(id,name,color)
FROM '/tmp/scripts/data/wine.csv' DELIMITER ';' CSV HEADER;
COPY wine_price(id,garden_id,wine_id,price)
FROM '/tmp/scripts/data/wine_price.csv' DELIMITER ';' CSV HEADER;
COPY wine_on_discount(wine_price_id,discount,valid_until)
FROM '/tmp/scripts/data/wine_on_discount.csv' DELIMITER ';' CSV HEADER;

COPY juice(id,name)
FROM '/tmp/scripts/data/juice.csv' DELIMITER ';' CSV HEADER;
COPY juice_price(id,garden_id,juice_id,price)
FROM '/tmp/scripts/data/juice_price.csv' DELIMITER ';' CSV HEADER;
COPY juice_on_discount(juice_price_id,discount,valid_until)
FROM '/tmp/scripts/data/juice_on_discount.csv' DELIMITER ';' CSV HEADER;
