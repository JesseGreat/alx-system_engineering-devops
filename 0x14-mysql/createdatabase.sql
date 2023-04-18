--create a database, table and grant user all access on the database
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (id INT PRIMARY KEY, name VARCHAR(50));
INSERT INTO nexus6 (id, name) VALUES (1, 'Roy Batty');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
