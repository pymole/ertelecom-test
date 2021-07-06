CREATE TABLE address (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    apartments_count int,
    floors_count int,
    entrances_count int,
    campus_id int NOT NULL REFERENCES campus(id)
);