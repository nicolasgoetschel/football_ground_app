DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS football_grounds;
DROP TABLE IF EXISTS leagues;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),   
    flag VARCHAR(255), 
    league VARCHAR(255)
);