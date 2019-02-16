#! /usr/bin/env python3
# coding: utf-8

import Classes
from Classes.Off_api import Off_api
from Classes.Db_module import Db_module
from init import NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS, \
    USER, PASSWORD, DATABASE, HOST, PORT

api = Off_api(NUMBER_OF_CATEGORIES, NUMBER_OF_PRODUCTS)
api.getdata()

db = Db_module(USER, PASSWORD, DATABASE, HOST, PORT)

db.feeddb(api.cats)

del db
