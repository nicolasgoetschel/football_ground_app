DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS football_grounds;
DROP TABLE IF EXISTS leagues;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    flag VARCHAR(255), 
    league VARCHAR(255)
);

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    logo VARCHAR(255), 
    football_ground VARCHAR(255)
);

CREATE TABLE football_grounds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    team VARCHAR(255), 
    location VARCHAR(255),
    capacity VARCHAR(255),
    visited BOOLEAN
);