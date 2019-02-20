#! /usr/bin/env python3
# coding: utf-8

""" Main script to launch the program """

import Classes
from Classes.Db_module import Db_module
from Classes.Menu import Menu
from init import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, \
    USER, PASSWORD, DATABASE, HOST, PORT


class Main:
    """ Class that launch the program """

    menu = Menu()
    menu.clear()
    pseudo = input("Entrez votre pseudo: ")
    db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
    if (pseudo == "root"):
        menu.menu_root(pseudo, db)
    elif (db.get_user(pseudo)):
        menu.menu(pseudo, db)
    else:
        db.create_user(pseudo)
        menu.menu(pseudo, db)
    del db

if __name__ == "__main__":
    program = Main()
