#! /usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector
import json

cat_url = "https://fr.openfoodfacts.org/categories.json"
r = requests.get(cat_url)
all_cat = r.json()

# with open("C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json", \
#   "w", encoding="utf-8") as outfile:
#     json.dump(all_cat, outfile)

url = "https://world.openfoodfacts.org/cgi/search.pl?search_terms=president&search_simple=1&action=process&json=1"
r = requests.get(url)
president = r.json()
with open("C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json",
   "w", encoding="utf-8") as outfile:
     json.dump(president, outfile)

cats = []
# id_cat = 0
for tag in all_cat["tags"][:20]:
    # print(tag["name"])
    # id_cat += 1
    # name = tag["name"]
    # url = tag["url"]
    # cats.append({"id_cat": id_cat, "name_cat": name_cat, "url_cat": url_cat})
    cats.append({"name": tag["name"], "url": tag["url"]})

# search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
# options = {"tagtype_0": "categories",
#     "tag_contains_0": "contains",
#     "tag_0": "Aliments et boissons à base de végétaux",
#     "page_size": "20",
#     "action": "process",
#     "json": "1"}
# r = requests.get(search_url, params=options)
# all_products = r.json()
# all_products["products"][0]
# with open("C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json", \
#   "w", encoding="utf-8") as outfile:
#     json.dump(all_products["products"][0], outfile)

# "product_name_fr"
# "ingredients_text_fr"
# "nutrition_grade_fr"
# "url"
# "stores"

# search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
# options = {
#     "tagtype_0": "categories",
#     "tag_contains_0": "contains",
#     "tag_0": "Desserts",
#     "page_size": "20",
#     "action": "process",
#     "json": "1"}
# r = requests.get(search_url, params=options)
# all_prod = r.json()

# with open("C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json", \
#   "w", encoding="utf-8") as outfile:
#     json.dump(all_prod["products"], outfile)

for cat in cats:
    # print(cat["name_cat"])
    search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
    options = {
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": cat["name"],
        "page_size": "20",
        "action": "process",
        "json": "1"}
    r = requests.get(search_url, params=options)
    all_prod = r.json()
    # print(all_prod["products"][1]["product_name_fr"])
    # for p in all_prod["products"][:2]:
    #     print(p["product_name_fr"])
    products = []
    for product in all_prod["products"][:2]:
        # name_prod = product["product_name_fr"]
        # description_prod = product["ingredients_text_fr"]
        # grade_prod = product["nutrition_grade_fr"]
        # url_prod = product["url"]
        # stores_prod = product["stores"]
        # products.append({
        #     "name_prod": name_prod,
        #     "description_prod": description_prod,
        #     "grade_prod": grade_prod,
        #     "url_prod": url_prod,
        #     "stores_prod": stores_prod})
        products.append({
            "name": product["product_name_fr"],
            "description": product["ingredients_text_fr"],
            "grade": product["nutrition_grade_fr"],
            "url": product["url"],
            "stores": product["stores"]})
    # print(products)
    cat["products"] = products

# import mysql.connector
mydb = mysql.connector.connect(
    user="svc_oc_p5",
    password="passw0rd",
    database="OC_P5",
    host="172.29.29.20",
    port=3306
)

print(mydb)
mycursor = mydb.cursor()

# sql_insert_cat = "INSERT INTO Category (name, url) VALUES (%s, %s)"
# cat_toinsert = ("test_name", "test@url.fr")
# mycursor.execute(sql_insert_cat, cat_toinsert)
# mydb.commit()
# cat_name = "test_name"
# mycursor.execute("SELECT id FROM Category WHERE name = %s", (cat_name,))
# cat_id = mycursor.fetchall()[0][0]
# prod_toinsert = [("test1", "blablabla", 5, "test1@off.fr", "super u", cat_id),
#                  ("test2", "blablablablou", 3, "test2@off.fr", "super u", cat_id),]
# sql_insert_prod = "INSERT INTO Product (name, desription, grade, url, \
# stores, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
# mycursor.executemany(sql_insert_prod, prod_toinsert)
# mydb.commit()


for cat in cats:
    sql_insert_cat = "INSERT INTO Category (name, url) VALUES (%s, %s)"
    cat_toinsert = (cat["name"], cat["url"])
    mycursor.execute(sql_insert_cat, cat_toinsert)
    mydb.commit()
    cat_name = cat["name"]
    mycursor.execute("SELECT id FROM Category WHERE name = %s", (cat_name,))
    cat_id = mycursor.fetchall()[0][0]
    prod_toinsert = []
    for prod in cat["products"]:
        prod_toinsert.append((
            prod["name"],
            prod["description"],
            prod["grade"],
            prod["url"],
            prod["stores"],
            cat_id))
    # prod_toinsert.append(,)
    sql_insert_prod = "INSERT INTO Product (name, description, grade, url, \
    stores, id_category) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql_insert_prod, prod_toinsert)
    mydb.commit()

