# coding: utf-8
import requests, json, os

cat_url = "https://fr.openfoodfacts.org/categories.json"
r = requests.get(cat_url)
all_cat = r.json()

# with open('C:/Users/Nico/Documents/Openclassrooms/P5/Projet/test.json', 'w', encoding="utf-8") as outfile:
    # json.dump(result, outfile)

Cat = {}
for tag in all_cat['tags'][:20]:
    # print(tag["name"])
    name = tag['name']
    url = tag['url']
    Cat.append({"name":name, "url":url})

search_url = "https://fr.openfoodfacts.org/cgi/search.pl"

options = {'search_terms':{}}, 'page_size':'20', 'json':'1'}
r = requests.get(search_url, params=options)

