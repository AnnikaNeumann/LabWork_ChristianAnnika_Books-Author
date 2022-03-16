DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    language VARCHAR(255),
    author VARCHAR(255),
    release INT

);

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    country VARCHAR(255)
);

