CREATE DATABASE Birds CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE Cats CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

SHOW TABLES FROM Birds;

CREATE TABLE Cats.table_name LIKE Birds.table_name;
INSERT INTO Cats.table_name SELECT * FROM Birds.table_name;

DROP DATABASE Birds;

DROP DATABASE Cats;

CREATE DATABASE IF NOT EXISTS VegFruits
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE VegFruits;

CREATE TABLE Items (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  type ENUM('овощ', 'фрукт') NOT NULL,
  color VARCHAR(50) NOT NULL,
  calories INT UNSIGNED NOT NULL,
  description TEXT,
  UNIQUE (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SELECT * FROM Items;

SELECT * FROM Items WHERE type='овощ';

SELECT * FROM Items WHERE type='фрукт';

SELECT name FROM Items;

SELECT DISTINCT color FROM Items;

SELECT * FROM Items WHERE type='фрукт' AND color='красный';

SELECT * FROM Items WHERE type='овощ' AND color='зеленый';
