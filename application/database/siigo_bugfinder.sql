CREATE SCHEMA siigo_bugfinder;
USE siigo_bugfinder;

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(200),
    is_confirmed BOOLEAN DEFAULT 0
);

CREATE TABLE cards(
	id INT AUTO_INCREMENT PRIMARY KEY,
    category INT, 
    name CHAR(20)
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
    
INSERT INTO categories(name) VALUES("developer"), ("module"), ("error");

INSERT INTO cards(category, name) VALUES(1, "Pedro"), (1, "Juan"), (1, "Carlos"), (1, "Juanita"), (1, "Antonio"), (1, "Carolina"), (1, "Manuel"),
										(2, "Nómina"), (2, "Facturación"), (2, "Recibos"), (2, "Comprobante Contable"), (2, "Usuarios"), (2, "Contabilidad"),
                                        (3, "404"), (3, "Stack Overflow"), (3, "Memory out of range"), (3, "Null pointer"), (3, "Syntax error"), (3, "Encoding error");