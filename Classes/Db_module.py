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

    def query(self, query, params):
        return self.cursor.execute(query, params)

    def __del__(self):
        self.connection.close()

    def feeddb(self, cats):
        """ Function that takes a list of categories with their associated
        products to feed the database """

        for cat in cats:
            sql_insert_cat = "INSERT INTO Category (name, url) VALUES (%s, %s)"
            cat_toinsert = (cat["name"], cat["url"])
            self.cursor.execute(sql_insert_cat, cat_toinsert)
            self.connection.commit()
            cat_name = cat["name"]
            self.cursor.execute("SELECT id FROM Category WHERE name = %s", (cat_name,))
            cat_id = self.cursor.fetchall()[0][0]
            prod_toinsert = []
            for prod in cat["products"]:
                prod_toinsert.append((
                    prod["name"],
                    prod["description"],
                    prod["grade"],
                    prod["url"],
                    prod["stores"],
                    cat_id))
            sql_insert_prod = "INSERT INTO Product (name, description, grade, url, \
            stores, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(sql_insert_prod, prod_toinsert)
            self.connection.commit()
