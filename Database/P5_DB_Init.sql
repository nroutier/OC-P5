-- Creating the database
CREATE DATABASE OC_P5 CHARACTER SET 'utf8';

-- Working on the database
USE OC_P5;


-- Creating Tables

CREATE TABLE User (
    id INT UNSIGNED AUTO_INCREMENT,
    pseudo VARCHAR(100) NOT NULL,
    password CHAR(40),
    PRIMARY KEY(id),
    UNIQUE INDEX ind_pseudo(pseudo)
) ENGINE=InnoDB;

CREATE TABLE Category (
	id INT UNSIGNED AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	url VARCHAR(100) NOT NULL,
	PRIMARY KEY(id),
    INDEX ind_name (name)
) ENGINE=InnoDB;

CREATE TABLE Product (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
	url VARCHAR(100) NOT NULL,
    desription TEXT NOT NULL,
    note INT(4),
    PRIMARY KEY(id),
    INDEX ind_name (name),
    INDEX ind_note (note)
) ENGINE=InnoDB;

CREATE TABLE Shop (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(300),
    PRIMARY KEY(id),
    INDEX ind_name(name)
) ENGINE=InnoDB;

CREATE TABLE Shop_prd(
    id_product INT UNSIGNED,
    id_shop INT UNSIGNED,
    PRIMARY KEY(id_product, id_shop)
) ENGINE=InnoDB;

CREATE TABLE Cat_prd(
    id_product INT UNSIGNED,
    id_category INT UNSIGNED,
    PRIMARY KEY(id_product, id_category)
) ENGINE=InnoDB;

-- Creating Foreign keys

ALTER TABLE Shop_prd 
ADD CONSTRAINT fk_shop_prd_prd FOREIGN KEY (id_product) REFERENCES Product(id),
ADD CONSTRAINT fk_shop_prd_shop FOREIGN KEY (id_shop) REFERENCES Shop(id);

ALTER TABLE Cat_prd
ADD CONSTRAINT fk_cat_prd_prd FOREIGN KEY (id_product) REFERENCES Product(id),
ADD CONSTRAINT fk_cat_prd_cat FOREIGN KEY (id_category) REFERENCES Category(id);