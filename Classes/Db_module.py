#! /usr/bin/env python3
# coding: utf-8

""" Module that defines the class Db_module """

import mysql.connector
from init import USER, PASSWORD, DATABASE, HOST, PORT


class Db_module:
    """ Class that handles the interface with the application database """

    def __init__(self, user, password, database, host, port):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        # self.cursor.close()
        self.connection.close()

    def feeddb(self, cats):
        """ Function that takes a list of categories with their associated
        products to feed the database """

        for cat in cats:
            sql_insert_cat = "INSERT INTO Category (name, url) VALUES (%s, %s)"
            cat_toinsert = (cat, cats[cat]["url"])
            self.cursor.execute(sql_insert_cat, cat_toinsert)
            self.connection.commit()
            self.cursor.execute(
                "SELECT id FROM Category WHERE name = %s",
                (cat,))
            cat_id = self.cursor.fetchall()[0][0]
            prod_toinsert = []
            for prod in cats[cat]["products"]:
                prod_toinsert.append((
                    prod,
                    cats[cat]["products"][prod]["description"],
                    cats[cat]["products"][prod]["grade"],
                    cats[cat]["products"][prod]["url"],
                    cats[cat]["products"][prod]["stores"],
                    cat_id))
            sql_insert_prod = "INSERT INTO Product (name, description, grade, url, \
            stores, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(sql_insert_prod, prod_toinsert)
            self.connection.commit()

    def get_categories(self, nb):
        query = ("SELECT * FROM Category LIMIT %s")
        self.cursor.execute(query, (nb,))
        return self.cursor.fetchall()

    def get_products(self, cat, nb):
        query = ("SELECT DISTINCT prd.name, prd.description, prd.grade, \
            prd.url, prd.stores, cat.name \
            FROM Product AS prd \
            INNER JOIN Category AS cat ON prd.id_category = cat.id \
            WHERE cat.name = %s ORDER BY prd.grade DESC LIMIT %s")

        self.cursor.execute(query, (cat, nb,))
        return self.cursor.fetchall()

    def get_bestproduct(self, cat):
        query = ("SELECT prd.name, prd.description, prd.grade, prd.url, prd.stores, \
            cat.name, cat.id \
            FROM Product AS prd \
            INNER JOIN Category AS cat ON prd.id_category = cat.id \
            WHERE cat.name = %s ORDER BY prd.grade LIMIT 1")

        self.cursor.execute(query, (cat,))
        return self.cursor.fetchall()[0]

    def create_user(self, pseudo):
        query = ("INSERT INTO User (pseudo) VALUES (%s)")
        self.cursor.execute(query, (pseudo,))
        self.connection.commit()

    def get_user(self, pseudo):
        query = ("SELECT pseudo FROM User WHERE pseudo = %s")
        self.cursor.execute(query, (pseudo,))
        return self.cursor.fetchall()

    def resetdb(self):
        query = ("DELETE FROM Saved_product")
        self.cursor.execute(query)
        self.connection.commit()
        query = ("DELETE FROM Product")
        self.cursor.execute(query)
        self.connection.commit()
        query = ("DELETE FROM Category")
        self.cursor.execute(query)
        self.connection.commit()
        query = ("DELETE FROM User")
        self.cursor.execute(query)
        self.connection.commit()
        query = ("ALTER TABLE Category AUTO_INCREMENT = 0")
        self.cursor.execute(query)
        query = ("ALTER TABLE Product AUTO_INCREMENT = 0")
        self.cursor.execute(query)
        query = ("ALTER TABLE Saved_product AUTO_INCREMENT = 0")
        self.cursor.execute(query)
        query = ("ALTER TABLE User AUTO_INCREMENT = 0")
        self.cursor.execute(query)
        self.connection.commit()
        query = ("INSERT INTO User (pseudo) VALUES ('root')")
        self.cursor.execute(query)
        self.connection.commit()

    def save_product(self, name, cat, pseudo):
        query_prd = ("SELECT id FROM Product WHERE name = %s \
            AND id_category = %s")
        self.cursor.execute(query_prd, (name, cat,))
        id_prd = self.cursor.fetchall()
        query_user = ("SELECT id FROM User WHERE pseudo = %s")
        self.cursor.execute(query_user, (pseudo,))
        id_user = self.cursor.fetchall()
        query = ("INSERT INTO Saved_product (id_product, id_user) VALUES \
            (%s, %s)")
        self.cursor.execute(query, (id_prd[0][0], id_user[0][0],))
        self.connection.commit()

    def get_savedproducts(self, pseudo):
        # query_user = ("SELECT id FROM User WHERE pseudo = %s")
        # self.cursor.execute(query_user, (pseudo,))
        # id_user = self.cursor.fetchall()
        query = ("SELECT prd.name FROM Product AS prd \
            INNER JOIN Saved_product AS sp \
                ON prd.id = sp.id_product \
                    INNER JOIN User AS usr ON sp.id_user = usr.id \
                        WHERE usr.pseudo = %s")
        self.cursor.execute(query, (pseudo,))
        return self.cursor.fetchall()
