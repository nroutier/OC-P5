#! /usr/bin/env python3
# coding: utf-8

""" Module that defines the class Off_api """

import requests


class Get_data_from_api:
    """ Class used to get the data from Open Food Fact API """

    def __init__(self, nb_cat, nb_prod):
        self.cats = {}
        self.nb_cat = nb_cat
        self.nb_prod = nb_prod

    def getdata(self):

        """ Function that gets data from openfoodfact api
        and return a dictionnary of categories with products """

        cat_url = "https://fr.openfoodfacts.org/categories.json"
        r = requests.get(cat_url)
        all_cat = r.json()

        for tag in all_cat["tags"]:
            if(self.cats.__len__() >= self.nb_cat):
                break
            if("Aliment" not in tag["name"]):
                cat_name = tag["name"]
                self.cats[cat_name] = {"url": tag["url"], "products": {}}

        for key in self.cats:
            search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
            options = {
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": key,
                "page_size": "100",
                "action": "process",
                "json": "1"}
            r = requests.get(search_url, params=options)
            all_prod = r.json()

            for product in all_prod["products"]:
                if(self.cats[key]["products"].__len__() >= self.nb_prod):
                    break
                if(
                    (product.get("nutrition_grade_fr") is not None) and
                        (product.get("product_name_fr") is not None)):
                        if(
                            (product["product_name_fr"] != "") and
                                (product["stores"] != "")):
                            p_name = product["product_name_fr"]
                            self.cats[key]["products"][p_name] = {
                                "description":
                                    product["ingredients_text_fr"],
                                "grade": product["nutrition_grade_fr"],
                                "url": product["url"],
                                "stores": product["stores"]
                                }
