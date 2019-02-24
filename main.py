#! /usr/bin/env python3
# coding: utf-8

""" Main script to launch the program """

import Classes
from Classes.Menu import Menu


class Main:
    """ Class that launch the program """
    menu = Menu()
    menu.clear()
    pseudo = input("Entrez votre pseudo: ")
    menu.user(pseudo)

if __name__ == "__main__":
    program = Main()
