CREATE TABLE backbone_network (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    central_head_station_id int NOT NULL REFERENCES central_head_station(id)
);