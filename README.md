# All About Posgres dB

postgresql is deprecated -> postgresql@14
How to start and stop postgres from the cli

- start
  - brew services start postgresql
- stop
  - brew services stop postgresql

Datatypes

- Serial, or BIGSERIAL
- VARCHAR
- INTEGER

Constraints
They can be applied to both the table and the columns inside.

- Not Null: values cannot be Null
- Unique: Values unique across the rows
- Primary Key: unique id of each row
- Foreign Key: Links to another table
- Check: data must satisfy boolean expression

- commands
  - SELECT
  - FROM
  - example
    - SELECT username FROM tablename
  - contents of table
    - ROWS = record
    - COLUMN = fields
- relationships between tables

POSTGRES

- features
  - open source
  - reliable
  - Logging in
    - $ psql
  
  - How to check role permissions?

  - How to CREATE DATABASE
    - alvinlim=# CREATE DATABASE dbname; # don't forget the semicolon
    - If successful you will get a response 'CREATE DATABASE'
  - How to DROP database
    - this delete the dB!
    - It works when no one is still accessing the db
  
```bash
odoo15a=# DROP DATABASE test2;
diceroll=# DROP DATABASE test;
DROP DATABASE
```

How to connect to db

- from cli
  - $ psql -h localhost -p 5432 -U alvinlim database_name
  - alvinlim@coolhandsg-iMac ~ % psql -h localhost -p 5432 -U postgres test
  - the name of db will appear on the left if successful
- inside pg
  - \c database_name

```bash
diceroll=# \c test
psql (14.7 (Homebrew), server 13.3)
You are now connected to database "test" as user "postgres".
```

How to terminate sessions from cli?

How to CREATE TABLE

- need table name
- column names
- columns need datatype
  
```bash
test=# CREATE TABLE person (
test(# id BIGSERIAL NOT NULL PRIMARY KEY,
test(# first_name VARCHAR(50) NOT NULL,
test(# last_name VARCHAR(50) NOT NULL,
test(# gender VARCHAR(7) NOT NULL,
test(# date_of_birth DATE NOT NULL,
test(# email VARCHAR(50) );
CREATE TABLE
```

How to check tables in db (check relations)

- \d
- \dt (just tables, no sequences)

How to check the columns in a table by specifying the table in mind

- \d db_name
- test=# \d person

How to DROP TABLE

```bash
test=# DROP TABLE person;
DROP TABLE
```

How to add constraints in our table creation

- datatype
- eg: BIGSERIAL auto-increments

How to add records to the table

  ```bash
test=# INSERT INTO person (first_name, last_name, gender, date_of_birth)
test-# VALUES ('Anne', 'Smith','FEMALE',date '1988-01-09');
INSERT 0 1
```

The response 'INSERT 0 1' shows success

How to show records in table

```bash
test=# SELECT * FROM person;
id | first_name | last_name | gender | date_of_birth |     email      
----+------------+-----------+--------+---------------+----------------
   1 | Anne       | Smith     | FEMALE | 1988-01-09    | 
   2 | Jake       | Jones     | MALE   | 1990-12-31    | jake@gmail.com
(2 rows)
```

- How to fill up the table with random data
  - Use mockaroo.com
  - download the file created
  - open it in vs code

How to delete or DROP TABLE

```bash
test=# DROP TABLE person;
DROP TABLE

How to filter

```bash
test=# SELECT * FROM person WHERE gender = 'Male';
```

How to select and view once & order DESC

```bash
test=# SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth DESC;
```

How to select and view and order by more than one column

```bash
test=# SELECT * FROM person WHERE gender = 'Male' and country_of_birth ='Poland';
```

How to filter by more than one value using ( ... = ... OR ... = ... )

```bash
test=# SELECT * FROM person WHERE gender = 'Male' and (country_of_birth = 'Poland' OR country_of_birth ='China');
```

How to limit the results

```bash
test=# SELECT * FROM person LIMIT 10;
```

How to limit the results with offset

```bash
test=# SELECT * FROM person OFFSET 5 LIMIT 5;
```

How to add more values to filter easily

```bash
test=# SELECT * 
FROM person
WHERE country_of_birth IN ('China', 'Brazil','Portugal') ORDER BY country_of_birth;
```

How to filter a range (e.g. Date)

```bash
test=# SELECT * FROM person
test-# WHERE date_of_birth
test-# BETWEEN DATE '2020-01-01' and '2023-01-01'; 1:38:09
```

## References

[video on postgres](https://www.youtube.com/watch?v=Q8iYj2ypWss)