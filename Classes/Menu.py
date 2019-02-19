#! /usr/bin/env python3
# coding: utf-8

""" Module that defines the class Menu """

import os


class Menu():
    """ Class used to generate the different Menus"""

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def print_product(self, product):
        print("Détail de l'aliment:")
        print("____________________")
        print("Nom du produit: ", product[0], "  |  Note: ", product[2])
        print("Catégorie: ", product[5])
        print("url: ", product[3])
        print("Magasins: ", product[4])
        print("Description: ", product[1])
        print("____________________")

    def menu(self, user, db):
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
                self.clear()
                print("Vous devez entrer le chiffre 1 ou 2")
                print("")
        if inp == 1:
            self.clear()
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
                    self.clear()
                    print(
                        "Vous devez entrer un chiffre correspondant",
                        " à une catégorie")
                    print("")
            self.clear()
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
                if inp in range(1, 11):
                    break
                else:
                    self.clear()
                    print(
                        "Vous devez entrer un chiffre correspondant",
                        "à un produit")
                    print("")
            self.clear()
            product = products[inp - 1]
            self.print_product(product)
            if products[inp - 1][2] != "a":
                bestproduct = db.get_bestproduct(products[inp - 1][5])
                print("")
                print(
                    "Vous pourriez remplacer cet aliment par le suivant",
                    "qui est mieux noté:")
                print("")
                self.print_product(bestproduct)
                while True:
                    inp = input("Souhaitez-vous sauvegarder ce substitut ? \
    O/N: ")
                    if (inp in ["o", "O"]):
                        db.save_product(bestproduct[0], bestproduct[6], pseudo)
                        break
                    elif (["n", "N"]):
                        break
                    else:
                        self.clear()
                        print("Vous devez répondre par 'O' ou 'N'")
                        print("")
            else:
                print("Cet aliment possède la note la plus haute, bon choix")
            del db
        elif inp == 2:
            self.clear()
            saved_products = db.get_savedproducts(pseudo)
            print("Voici les aliments que vous avez sauvegardé: ")
            print("____________________________________________")
            for prd in saved_products:
                print(prd[0])

    def menu_root(self, user, db, api):
        pseudo = user
        while True:
            print("Vous êtes connecté en tant qu'administrateur, voulez vous:")
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
                self.clear()
                print("Vous devez entrer un chiffre en 1 et 3")
                print("")
        if inp == 1:
            api.getdata()
            db.feeddb(api.cats)
            self.menu(pseudo, db)
        elif (inp == 2):
            db.resetdb()
        elif (inp == 3):
            self.menu(pseudo, db)
