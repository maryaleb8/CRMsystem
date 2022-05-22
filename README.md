# Functionality:
Admins have an opportunity to add new order to database with order status and comments

# Technical details:

## back-end
In this API, there is an ability to add an order, to change an order, to delete an order. To view all orders from the database, I implemented /posts endpoint.

## front-end
I made a window for the administrator, with which you can easily add a new order. Also I made page with all posts and their description. I made two pages with additional information.

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
chmod +x app.py
```
Execute:
```
python3 app.py
```
