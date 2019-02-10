# OC project 5 - Use OpenFoodFacts public data

This project is about creating a program to retrieve from OpenFoodFacts API a type of "junk" food and get a healthy substitute with all needed information about this new product (description, a shop where to buy it and a link to the OpenFoodFacts webpage regarding this product), the user will then have the possibility to save this healthy product in a local MySQL database.

## Description of the user's route

The user is on the terminal. The terminal display two choices:

1. Which food do you want to replace ?
2. Find my healthy substitued food.

When the user select 1. The application awser these questions to the user and the user select these responses :
* Select the category. [Further proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* Select food. [Further proposals are associated to a number. The user enter the corresponding number and press "Enter".]
* The application propose a substitute, its description, a store to buy it and a link to the page Open Food Facts of this food.
* The user can saved the result in the database.

## Functionality

1. Search of food in the database Open Food Facts.
2. The user use the application in the terminal.
3. If the user enter a character that is not a number, the application repeat the question again.
4. The research occurs on a MySQL base.

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
Execute this Python Script to : `To come`
`$ cd myproject`
`$ pipenv install requests`
`$ pipenv run python main.py`

