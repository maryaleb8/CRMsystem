# To start with

Run the command line: python3 app.py

# Functionality:
Admins have an opportunity to add new order to database with order status and comments

# Technical details:

## back-end
In this project I use the REST-API architecture. In this API, there is an ability to add an order (/add_new_order), to change an order (/update_order), to delete an order (/delete_order). To view all orders from the database, I implemented /all_orders endpoint. (commands update and delete don't exist now)

## front-end
I made a convenient window for the administrator, with which you can easily add a new order.

# Usage (Linux):

Open terminal.
Make sure you have python3 and flask, flask_sqlalchemy, datetime installed:
```
sudo apt install python3
pip install flask
pip install flask_sqlalchemy
pip install datetime
```
Download the project:
```
git clone https://github.com/maryaleb8/CRMsystem.git
cd CRMsystem
chmod +x main.py
```
Execute:
```
python3 app.py
```
