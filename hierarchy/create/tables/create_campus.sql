CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    address varchar(255),
    name varchar(255),
    backbone_network_id int NOT NULL REFERENCES backbone_network(id)
);