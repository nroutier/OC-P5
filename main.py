#! /usr/bin/env python3
# coding: utf-8

import os
import Classes
from Classes.Off_api import Off_api
from Classes.Db_module import Db_module
from init import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, \
    USER, PASSWORD, DATABASE, HOST, PORT


class Main:
    def cls():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    cls()
    while True:
        print(
            "1 - Alimenter la base de données avec les données d'Open Food",
            " Facts")
        print("2 - Quel aliment souhaitez-vous remplacer ?")
        print("3 - Retrouver mes aliments substitués")
        inp = input("Votre choix: ")
        try:
            inp = int(inp)
        except ValueError:
            pass
        if inp in range(1, 3):
            break
        else:
            cls()
            print("Vous devez entrer un chiffre en 1 et 3")
            print("")

    if inp == 1:
        api = Off_api(NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS)
        api.getdata()
        db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
        db.feeddb(api.cats)
        del db

    elif inp == 2:
        db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
        cls()
        cats = db.get_categories(10)
        while True:
            print("Vous avez le choix entre les catégories suivantes:")
            print("__________________________________________________")
            print("")
            for i, cat in enumerate(cats):
                print(i+1, ". ", cat[1])
            print("")
            inp = input("Sélectionez la catégorie: ")
            try:
                inp = int(inp)
            except ValueError:
                pass
            if inp in range(1, 10):
                break
            else:
                cls()
                print(
                    "Vous devez entrer un chiffre correspondant",
                    " à une catégorie")
                print("")
        cls()
        products = db.get_products(cats[int(inp) - 1][1], 10)
        while True:
            print("Vous avez le choix entre les aliments suivants:")
            print("_______________________________________________")
            print("")
            for i, product in enumerate(products):
                print(i+1, ". ", product[0])
            inp = input("Sélectionnez l'aliment: ")
            try:
                inp = int(inp)
            except ValueError:
                pass
            if inp in range(1, 10):
                break
            else:
                cls()
                print(
                    "Vous devez entrer un chiffre correspondant",
                    " à un produit")
                print("")
        cls()
        print("Détail de l'aliment:")
        print("____________________")
        print("")
        print("Nom du produit: ", products[inp - 1][0])
        print("Description: ", products[inp - 1][1])
        print("Note: ", products[inp - 1][2])
        print("url: ", products[inp - 1][3])
        print("Magasins: ", products[inp - 1][4])
        print("Catégorie: ", products[inp - 1][5])
        print("")
        print("____________________")
        if products[inp - 1][2] != "a":
            bestproduct = db.get_bestproduct(products[inp - 1][5])
            print("")
            print(
                "Vous pourriez remplacer cet aliment le suivant",
                " qui est mieux noté:")
            print("")
            print("Nom du produit: ", bestproduct[0])
            print("Description: ", bestproduct[1])
            print("Note: ", bestproduct[2])
            print("url: ", bestproduct[3])
            print("Magasins: ", bestproduct[4])
            print("Catégorie: ", bestproduct[5])
            print("")

        del db

if __name__ == "__main__":
    program = Main()
