--create a replica user
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';           "GRANT SELECT ON mysql.* TO 'holberton_user'@'localhost'; FLUSH PRIVILEGES;"
