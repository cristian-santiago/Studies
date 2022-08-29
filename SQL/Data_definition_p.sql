-- PostgreSQL - Data Definition Language (Movies database)


-- Creating the directors table;

CREATE TABLE directors (

    director_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30) NOT NULL,
    date_of_birth DATE,
    nationality VARCHAR(20)

);


-- Creating the actors table;
CREATE TABLE actors (

    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    gender CHAR(1),
    date_of_birth DATE
);

-- Creating the movies table (with foreign key)

CREATE TABLE movies (

    movie_id SERIAL PRIMARY KEY,
    movie_name VARCHAR(50) NOT NULL,
    movie_length INT,
    movie_lang VARCHAR(20),
    release_date DATE,
    age_certificate VARCHAR(5),
    director_id INT REFERENCES directors (director_id)

);

-- Creating the movie_revenues table

CREATE TABLE movie_revenues (

    revenue_id SERIAL PRIMARY KEY,
    movie_id INT REFERENCES movies (movie_id),
    domestic_takings NUMERIC(6,2),
    international_takings NUMERIC(6,2)
);

-- Creating the movie_actors table

CREATE TABLE movie_actors (
    movie_id INT REFERENCES movies (movie_id),
    actor_id INT REFERENCES actors (actor_id),
    PRIMARY KEY (movie_id, actor_id)
);


-- Modifying tables - Adding columns 

-- One column
ALTER TABLE user_examples
ADD COLUMN email VARCHAR(50) UNIQUE
-- Multiple column
ALTER TABLE books
ADD COLUMN pages INT NOT NULL,
ADD COLUMN title VARCHAR(50), 
ADD COLUMN editor VARCHAR(50);

-- Modifying tables -- Changing columns data type 

-- One column
ALTER TABLE user_examples
ALTER COLUMN email TYPE VARCHAR(60) UNIQUE;

-- Multiple column
ALTER TABLE books
ALTER COLUMN title TYPE VARCHAR(60),
ALTER COLUMN editor TYPE VARCHAR(60);

-- Deleting tables from a database

DROP TABLE table_name;

--

-- Challenge 1 

CREATE DATABASE owners_pets;

CREATE TABLE owners (
 
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    city VARCHAR(30),
    state CHAR(2)
);

CREATE TABLE pets (

    id SERIAL PRIMARY KEY,
    species VARCHAR(30),
    full_name VARCHAR(30),
    age INT,
    owner_id INT REFERENCES owners (id)

);

ALTER TABLE owners
ADD COLUMN email VARCHAR(50) ;

ALTER TABLE owners
ADD CONSTRAINT constraint_name UNIQUE(email);

ALTER TABLE owners (
ALTER COLUMN last_name TYPE VARCHAR(50));
