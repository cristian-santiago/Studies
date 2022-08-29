-- PostgreSQL -> Data Manipulation (Movies database)

-- Inserting Data into a table ( One row)

INSERT INTO table_name (column_name1, column_name2, column_name3)
VALUES ("value1", "value2", "value3");

-- Multiple rows

INSERT INTO table_name (column_name1, column_name2, column_name3)
VALUES ("value4", "value5", "value6"),
        ("value7", "value7", "value9");


-- Updating Data into a table
-- For better practicing, the column name that must be updated be the primary key, it will avoid updating many rows that matched.


UPDATE table_name
SET column_name = "new_value"
WHERE colum_pk = "value"; 


-- Updating multiple columns 

UPDATE table_name
SET column_name1 = "value1", column_name2 = "value2", colum_name3 = "value3"
WHERE column_pk = "value"; 


-- Deleting data from a table
-- For better practicing, the column name that must be deleted be the primary key, it will avoid deleting many rows that matched.

DELETE from table_name
WHERE column_name =  "value" 

-- Deleting all the Data from the table

DELETE FROM table_name;

-- Inserting Data into the Movie table (Challenge)

-- Owners table

INSERT INTO owners (first_name, last_name, city, state, email)
VALUES  ('Samuel', 'Smith', 'Boston', 'MA', 'samsmith@gmail.com')
        ('Emma', 'Jhonson', 'Seattle', 'WA', 'samsmith@gmail.com'),
        ('John', 'Oliver', 'New York', 'NY', 'johnoliver@gmail.com'),
        ('Olivia', 'Brown', 'San Francisco', 'CA', 'oliviabrown@gmail.com'),
        ('Simon', 'Smith', 'Dallas', 'TX', 'sismith@gmail.com')
        ( , 'Maxwell', , 'CA', 'lordmaxwell@gmail.com' );

-- Pets table 

INSERT INTO pets (species, full_name, age, owner_id)
VALUES ('Dog', 'Rex', 6, 1),
        ('Rabbit', 'Fluffy', 2, 5),
        ('Cat', 'Tom', 8, 2),
        ('Mouse', 'Jerry', 2, 2),
        ('Dog', 'Biggles', 4, 1),
        ('Tortoise', 'Squirtle', 42, 3);