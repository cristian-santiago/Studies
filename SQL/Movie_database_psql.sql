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