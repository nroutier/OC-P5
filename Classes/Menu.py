#! /usr/bin/env python3
# coding: utf-8

""" Module that defines the class Menu """

import os
import sys
import config
from config import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, USER, PASSWORD, \
    DATABASE, HOST, PORT
import Classes
from Classes.Get_data_from_api import Get_data_from_api
from Classes.Db_module import Db_module


class Menu():
    """ Class used to generate the different Menus"""

    def __init__(self):
        """ Function to initiate an object from Menu class """
        self.db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)

    def clear(self):
        """ Function that clears terminal screen """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def print_product(self, product):
        """ Function that prints a product in terminal """
        print("Détail de l'aliment:")
        print("____________________")
        print("Nom du produit: ", product[0], "  |  Note: ", product[2])
        print("Catégorie: ", product[5])
        print("url: ", product[3])
        print("Magasins: ", product[4])
        print("Description: ", product[1])
        print("____________________")

    def end_program(self, user):
        """ Function to end the program """
        while True:
            inp = input("Revenir au menu (O) ou quitter le programme (Q)")
            if (inp in ["o", "O"]):
                self.clear()
                self.menu(user)
            elif (inp in ["q", "Q"]):
                self.clear()
                print("Merci d'avoir utilisé le programme")
                sys.exit()
            else:
                print("Vous devez entrer O ou Q")

    def user(self, pseudo):
        """ Function that handles user menu redirection """
        if (pseudo == "root"):
            self.menu_root(pseudo)
        elif (self.db.get_user(pseudo)):
            self.menu(pseudo)
        else:
            self.db.create_user(pseudo)
            self.menu(pseudo)

    def menu(self, user):
        """ Function that generate the program menu """
        self.clear()
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
            cats = self.db.get_categories(10)
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
                if inp in range(1, 11):
                    break
                else:
                    self.clear()
                    print(
                        "Vous devez entrer un chiffre correspondant",
                        " à une catégorie")
                    print("")
            self.clear()
            products = self.db.get_products(cats[inp - 1][1], 10)
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
                bestproduct = self.db.get_bestproduct(products[inp - 1][5])
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
                        self.db.save_product(
                            bestproduct[0],
                            bestproduct[6],
                            user)
                        break
                    elif (["n", "N"]):
                        break
                    else:
                        self.clear()
                        print("Vous devez répondre par 'O' ou 'N'")
                        print("")
            else:
                print("Cet aliment possède la note la plus haute, bon choix")
                while True:
                    inp = input("Souhaitez-vous sauvegarder ce substitut ? \
O/N: ")
                    if (inp in ["o", "O"]):
                        self.db.save_product(
                            bestproduct[0],
                            bestproduct[6],
                            user)
                        break
                    elif (["n", "N"]):
                        break
                    else:
                        self.clear()
                        print("Vous devez répondre par 'O' ou 'N'")
                        print("")
            self.end_program(user)
        elif inp == 2:
            self.clear()
            saved_products = self.db.get_savedproducts(user)
            while True:
                print("Voici les aliments que vous avez sauvegardé: ")
                print("_________________________________________________")
                for i, prd in enumerate(saved_products):
                    print(i+1, ". ", prd[0])
                print("_________________________________________________")
                inp = input("Souhaitez-vous afficher les détails d'un aliment? \
O/N: ")
                if (inp in ["o", "O"]):
                    inp = input("Sélectionnez l'aliment: ")
                    try:
                        inp = int(inp)
                    except ValueError:
                        pass
                    if inp in range(1, saved_products.__len__() + 1):
                        saved_product = self.db.get_product(
                            saved_products[inp - 1][0])
                        self.print_product(saved_product[0])
                    else:
                        self.clear()
                        print(
                            "Vous devez entrer un chiffre correspondant",
                            "à un produit")
                        print("")
                elif (inp in ["n", "N"]):
                    break
                else:
                    print("Vous devez entrer O ou N")
            self.end_program(user)

    def menu_root(self, user):
        """ Function that generate the adminitrator menu """
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
            if (self.db.check_db()):
                print("La base de données a déjà été alimentée")
            else:
                api = Get_data_from_api(
                    NUMBER_OF_CATEGORIES,
                    NUMBER_OF_PRODUCTS)
                api.getdata()
                self.db.feeddb(api.cats)
                print("La base de données vient d'être alimentée")
                del api
        elif (inp == 2):
            self.db.resetdb()
        elif (inp == 3):
            self.menu(user)
