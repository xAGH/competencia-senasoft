CREATE SCHEMA siigo_bugfinder;
USE siigo_bugfinder;

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(200),
    is_confirmed BOOLEAN DEFAULT false
);

CREATE TABLE cards(
	id INT AUTO_INCREMENT PRIMARY KEY,
    category INT
);

CREATE TABLE categories(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name CHAR(15)
);

CREATE TABLE user_stats(
	user INT,
    games_played INT,
    games_won INT
);

ALTER TABLE cards
	ADD FOREIGN KEY (category) REFERENCES categories(id);