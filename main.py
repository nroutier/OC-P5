#! /usr/bin/env python3
# coding: utf-8

import os
import Classes
from Classes.Off_api import Off_api
from Classes.Db_module import Db_module
from init import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, \
    USER, PASSWORD, DATABASE, HOST, PORT


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Main:

    def menu(user):
        pseudo = user
        while True:
            print("1 - Quel aliment souhaitez-vous remplacer ?")
            print("2 - Retrouver mes aliments substitués")
            inp = input("Votre choix: ")
            try:
                inp = int(inp)
            except ValueError:
                pass
            if inp in range(1, 3):
                break
            else:
                clear()
                print("Vous devez entrer le chiffre 1 ou 2")
                print("")

        db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)

        if inp == 1:
            clear()
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
                    clear()
                    print(
                        "Vous devez entrer un chiffre correspondant",
                        " à une catégorie")
                    print("")
            clear()
            products = db.get_products(cats[inp - 1][1], 10)
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
                    clear()
                    print(
                        "Vous devez entrer un chiffre correspondant",
                        "à un produit")
                    print("")
            clear()
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
                    "Vous pourriez remplacer cet aliment par le suivant",
                    "qui est mieux noté:")
                print("")
                print("Nom du produit: ", bestproduct[0])
                print("Description: ", bestproduct[1])
                print("Note: ", bestproduct[2])
                print("url: ", bestproduct[3])
                print("Magasins: ", bestproduct[4])
                print("Catégorie: ", bestproduct[5])
                print("")
                print("____________________")
                print("")
                while True:
                    inp = input("Souhaitez-vous sauvegarder ce substitut ? \
O/N: ")
                    if (inp in ["o", "O"]):
                        db.save_product(bestproduct[0], bestproduct[6], pseudo)
                        break
                    elif (["n", "N"]):
                        break
                    else:
                        clear()
                        print("Vous devez répondre par 'O' ou 'N'")
                        print("")

            else:
                print("Cet aliment possède la note la plus haute, bon choix")

            del db
        elif inp == 2:
            clear()
            saved_products = db.get_savedproducts(pseudo)
            print("Voici les aliments que vous avez sauvegardé: ")
            print("____________________________________________")
            for prd in saved_products:
                print(prd[0])

    clear()
    pseudo = input("Entrez votre pseudo: ")
    db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
    if (pseudo == "root"):
        while True:
            print(
                "1 - Alimenter la base de données avec les données d'Open",
                "Food Facts")
            print("2 - Vider les tables de la base")
            print("3 - Lancer le programme")
            inp = input("Votre choix: ")
            try:
                inp = int(inp)
            except ValueError:
                pass
            if inp in range(1, 4):
                break
            else:
                clear()
                print("Vous devez entrer un chiffre en 1 et 3")
                print("")
        if inp == 1:
            api = Off_api(NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS)
            api.getdata()
            # db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)
            db.feeddb(api.cats)
            menu(pseudo)

        elif (inp == 2):
            db.resetdb()

        elif (inp == 3):
            menu(pseudo)

    elif (db.get_user(pseudo)):
        print("Bienvenue dans le programme", pseudo)
        menu(pseudo)
    else:
        db.create_user(pseudo)
        print("Bienvenue dans le programme", pseudo)
        menu(pseudo)

if __name__ == "__main__":
    program = Main()
