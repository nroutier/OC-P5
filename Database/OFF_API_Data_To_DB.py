# coding: utf-8
import requests
import json

cat_url = "https://fr.openfoodfacts.org/categories.json"
r = requests.get(cat_url)
all_cat = r.json()

# with open("C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json", \
#   "w", encoding="utf-8") as outfile:
#     json.dump(all_cat, outfile)

cats = []
id_cat = 0
for tag in all_cat["tags"][:20]:
    # print(tag["name"])
    id_cat += 1
    name_cat = tag["name"]
    url_cat = tag["url"]
    cats.append({"id_cat": id_cat, "name_cat": name_cat, "url_cat": url_cat})

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
      "tag_0": cat["name_cat"],
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
        name_prod = product["product_name_fr"]
        description_prod = product["ingredients_text_fr"]
        grade_prod = product["nutrition_grade_fr"]
        url_prod = product["url"]
        stores_prod = product["stores"]
        products.append({
            "name_prod": name_prod,
            "description_prod": description_prod,
            "grade_prod": grade_prod,
            "url_prod": url_prod,
            "stores_prod": stores_prod})
    # print(products)
    cat["products"] = products

for cat in cats:
    for prod in cat["products"]:
        print(prod["stores_prod"])