#! /usr/bin/env python3
# coding: utf-8

import Classes
from Classes.Off_api import Off_api
from Classes.Db_module import Db_module
from Classes.Menu import Menu
from init import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, \
    USER, PASSWORD, DATABASE, HOST, PORT


class Main:

    menu = Menu()
    menu.clear()
    pseudo = input("Entrez votre pseudo: ")
    db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
    api = Off_api(NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS)
    if (pseudo == "root"):
        print("Bienvenue dans le programme", pseudo, "!")
        menu.menu_root(pseudo, db, api)
    elif (db.get_user(pseudo)):
        print("Bienvenue dans le programme", pseudo, "!")
        menu.menu(pseudo, db)
    else:
        db.create_user(pseudo)
        print("Bienvenue dans le programme", pseudo, "!")
        menu.menu(pseudo, db)
    del db

if __name__ == "__main__":
    program = Main()
