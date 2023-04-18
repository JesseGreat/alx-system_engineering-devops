--Create user
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
--grant permission
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
