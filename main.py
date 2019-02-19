#! /usr/bin/env python3
# coding: utf-8

""" Main script to launch the program """

import Classes
from Classes.Get_off_data import Get_off_data
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
    api = Get_off_data(NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS)
    if (pseudo == "root"):
        menu.menu_root(pseudo, db, api)
    elif (db.get_user(pseudo)):
        menu.menu(pseudo, db)
    else:
        db.create_user(pseudo)
        menu.menu(pseudo, db)
    del db

if __name__ == "__main__":
    program = Main()
