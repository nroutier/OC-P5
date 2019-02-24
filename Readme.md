# OC project 5 - Use OpenFoodFacts public data

This project is about creating an application to retrieve from OpenFoodFacts API a type of "junk" food and get a healthy substitute with all needed information about this new product (description, a shop where to buy it and a link to the OpenFoodFacts webpage regarding this product), the user will then have the possibility to save this healthy product in a local MySQL database.

## Description of the user's route

Once the program is launched (see section 3), you will have to log in:

![user_login](https://github.com/nroutier/OC-P5/blob/master/images/login_user.png?raw=true)

The first time you log in, the program will create your user, then you will be able to log in again with the same pseudo to retreive the products you already saved.

The user is on the terminal. The terminal displays the user menu:

![user_menu](https://github.com/nroutier/OC-P5/blob/master/images/menu_user.png?raw=true)

When entering 1, the program will display the categories that you can choose from:

![user_menu_cats](https://github.com/nroutier/OC-P5/blob/master/images/menu_user_cats.png?raw=true)

Once you enter a number to select a category, you will have the select a product from this category:

![user_menu_products](https://github.com/nroutier/OC-P5/blob/master/images/menu_user_products.png?raw=true)

Then after entering the number for the product you want, the program will display its details and suggest a product with its details from the same category with a higher nutrition grade:

![user_menu_product](https://github.com/nroutier/OC-P5/blob/master/images/menu_user_prod.png?raw=true)

The program offers to the user to save the product in the database, so he will have the opportunity by entering 2 on the first menu to retreive his saved healthy products:

![user_menu_saved_products](https://github.com/nroutier/OC-P5/blob/master/images/menu_user_saved_products.png?raw=true)

## Functionality

1. Search food in the Open Food Facts database.
2. The user interact with the application through the terminal.
3. If the user enter a character that is not a number, the application must ask the question again.
4. The research occurs on a MySQL database.

## Getting started

### 1.Setting up the Database

To install your MySQL Database go to [MySQL Webpage](https://dev.mysql.com/doc/refman/8.0/en/installing.html)

Here is the Database schema: 

![Schema](https://github.com/nroutier/OC-P5/blob/master/images/MPD.png?raw=true)

SQL Script to initiate the database: [P5_DB_Init.sql](https://github.com/nroutier/OC-P5/blob/master/Database/P5_DB_Init.sql)

From MySQL console as "root": `SOURCE path\P5_DB_Init.sql`

### 2.Feed the database with OpenFoodFacts French data from the OpenFoodFacts API

The program is based on data stored on [Open Food Facts](https://fr.openfoodfacts.org/) website.

It uses the [Requests](http://docs.python-requests.org/en/master/) library to get the [Open Food Facts Categories Json file](https://fr.openfoodfacts.org/categories.json) to retrieve the categories of products and the [Open Food Facts API](https://en.wiki.openfoodfacts.org/API/Read/Search) to get the products for each category.

Then it uses the [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) to interact with the database.

#### The Administrator menu:

Once your database is created with all the tables (see section 1), you will need to feed the database with the data from Open Food Fact.

To do so, you will have to launch the program (see section 3) and log in as root:

![root_login](https://github.com/nroutier/OC-P5/blob/master/images/login_root.png?raw=true)

Once logged in, the Administrator menu will display:

![root_menu](https://github.com/nroutier/OC-P5/blob/master/images/menu_root.png?raw=true)

For a first use of the program, you will have to enter 1 to feed the database.

If you want to empty the tables with all data from Open Food Facts and created users (except from root), you can enter 2.

### 3.Launch the program

The program is using Python 3.7.1, make sure you have Python and pip installed.

I used pipenv [pipenv](https://pipenv.readthedocs.io/en/latest/install/), but you can choose other option like venv,
you will just have to addapt the install command below.

Clone this repository.

The program needs to be run from the program folder in the terminal,

Execute this Python Script to :

`$ pipenv install requests`

`$ pipenv install mysql-connector-python`

`$ pipenv run python main.py`
