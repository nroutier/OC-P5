#! /usr/bin/env python3
# coding: utf-8

""" Module that defines the class Off_api """

import requests


class Off_api:
    """ Class used to interact with Open Food Fact API """

    def __init__(self, nb_cat, nb_prod):
        self.cats = []
        self.nb_cat = nb_cat
        self.nb_prod = nb_prod

    def getdata(self):

        """ Function that gets data from openfoodfact api
        and return an array of categories with products """

        cat_url = "https://fr.openfoodfacts.org/categories.json"
        r = requests.get(cat_url)
        all_cat = r.json()

        for tag in all_cat["tags"][:self.nb_cat]:
            self.cats.append({"name": tag["name"], "url": tag["url"]})

        for cat in self.cats:
            search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
            options = {
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cat["name"],
                "page_size": "100",
                "action": "process",
                "json": "1"}
            r = requests.get(search_url, params=options)
            all_prod = r.json()
            products = []
            while(products.__len__() < self.nb_prod):
                for product in all_prod["products"]:
                    if (
                        (product.get("nutrition_grade_fr") is not None)
                            and (product["product_name_fr"] != "")):
                                products.append({
                                    "name": product["product_name_fr"],
                                    "description": product["ingredients_text_fr"],
                                    "grade": product["nutrition_grade_fr"],
                                    "url": product["url"],
                                    "stores": product["stores"]})
            cat["products"] = products
