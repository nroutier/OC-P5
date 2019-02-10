# OC project 5 - Use OpenFoodFacts public data

This project is about creating an application to retrieve from OpenFoodFacts API a type of "junk" food and get a healthy substitute with all needed information about this new product (description, a shop where to buy it and a link to the OpenFoodFacts webpage regarding this product), the user will then have the possibility to save this healthy product in a local MySQL database.

## Description of the user's route

The user is on the terminal. The terminal displays two choices:

1. Which food do you want to replace ?
2. Find my saved healthy substitued.

When the user selects 1. The application ask the following questions to the user for him to answer:
* Select the category. [Further proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* Select food. [Further proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* The application offer a substitute, its description, a store to buy it and a link to the Open Food Facts webpage for this food.
* The user can save the result in the database.

## Functionality

1. Search food in the Open Food Facts database.
2. The user interact with the application through the terminal.
3. If the user enter a character that is not a number, the application must ask the question again.
4. The research occurs on a MySQL database.

## Getting started

### 1.Setting up the Database

To install your MySQL Database go to [MySQL Webpage](https://dev.mysql.com/doc/refman/8.0/en/installing.html)

Here is the Database schema: 

![Schema](https://github.com/nroutier/OC-P5/blob/master/Database/MPD.png?raw=true)

SQL Script to initiate the database: [P5_DB_Init.sql](https://github.com/nroutier/OC-P5/blob/master/Database/P5_DB_Init.sql)

From MySQL console: `SOURCE path\P5_DB_Init.sql`

### 2.Filling up the database with OpenFoodFacts French data from the OpenFoodFacts API

[Open Food Facts API](https://en.wiki.openfoodfacts.org/API/Read/Search)


### 3.Launch the program
The program needs to be run in the terminal. 
Execute this Python Script to :

`$ cd myproject`

`$ pipenv install requests`

`$ pipenv run python main.py`

