-- Creating the database
CREATE DATABASE OC_P5 CHARACTER SET 'utf8';

-- Creating the user
CREATE USER 'username' IDENTIFIED BY 'password';

-- Giving all privelege to user svc_oc_p5
GRANT ALL PRIVILEGES ON OC_P5.* TO 'username';

-- Working on the database
USE OC_P5;


-- Creating Tables

CREATE TABLE Category (
	id INT UNSIGNED AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	url VARCHAR(500) NOT NULL,
	PRIMARY KEY(id),
    INDEX ind_name (name)
) ENGINE=InnoDB;

CREATE TABLE Product (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    grade VARCHAR(2),
	url VARCHAR(500) NOT NULL,
    stores VARCHAR(1000),
    id_category INT UNSIGNED NOT NULL,
    PRIMARY KEY(id),
    INDEX ind_name (name),
    INDEX ind_grade (grade)
) ENGINE=InnoDB;

CREATE TABLE User (
    id INT UNSIGNED AUTO_INCREMENT,
    pseudo VARCHAR(100) NOT NULL,
    PRIMARY KEY(id),
    INDEX ind_pseudo (pseudo)
) ENGINE=InnoDB;

CREATE TABLE Saved_product (
    id_product INT UNSIGNED NOT NULL,
    id_user INT UNSIGNED NOT NULL
) ENGINE=InnoDB;

-- Creating Foreign keys

ALTER TABLE Product
ADD CONSTRAINT fk_prd_cat FOREIGN KEY (id_category) REFERENCES Category(id);

ALTER TABLE Saved_product
ADD CONSTRAINT fk_sav_prd FOREIGN KEY (id_product) REFERENCES Product(id),
ADD CONSTRAINT fk_sav_user FOREIGN KEY (id_user) REFERENCES User(id);

-- Adding root user into User table
INSERT INTO User (pseudo) VALUE ("root");
