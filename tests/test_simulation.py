import mysql.connector
import json
import logging

def simulation():
    """
    Insert fictitious data into the database
    """
    with open("database/connection/config.json") as file:
        data = json.load(file)
        host = data["host"]
        user = data["user"]
        password = data["password"]

    mysql_connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = "RESTAURANT_MANAGEMENTSYSTEM"
    )
    cursor = mysql_connection.cursor()

    cursor.execute("""INSERT INTO ACCOUNT (id_account, username, password, email) 
                   VALUES (55, 'testtest', 'test', 'test');""")

    cursor.execute("""INSERT INTO CUSTOMER (name, address, cell_phone, account_id_account) 
                   VALUES 
                   ('George', 'City of Brazil', 123456789, 55),
                   ('Emma', 'City of Brazil', 123456789, 55),
                   ('Oliver', 'City of Brazil', 123456789, 55),
                   ('Muhammad', 'City of Brazil', 123456789, 55),
                   ('Sophia', 'City of Brazil', 123456789, 55),
                   ('Harry', 'City of Brazil', 123456789, 55),
                   ('Oscar', 'City of Brazil', 123456789, 55),
                   ('Abigail', 'City of Brazil', 123456789, 55),
                   ('John', 'City of Brazil', 123456789, 55),
                   ('Alice', 'City of Brazil', 123456789, 55),
                   ('Ava', 'City of Brazil', 123456789, 55),
                   ('Ella', 'City of Brazil', 123456789, 55),
                   ('Benjamin', 'City of Brazil', 123456789, 55),
                   ('Charlotte', 'City of Brazil', 123456789, 55),
                   ('Michael', 'City of Brazil', 123456789, 55),
                   ('Amelia', 'City of Brazil', 123456789, 55),
                   ('Daniel', 'City of Brazil', 123456789, 55),
                   ('Mia', 'City of Brazil', 123456789, 55),
                   ('Henry', 'City of Brazil', 123456789, 55),
                   ('Grace', 'City of Brazil', 123456789, 55),
                   ('Alexander', 'City of Brazil', 123456789, 55),
                   ('Liam', 'City of Brazil', 123456789, 55),
                   ('Avery', 'City of Brazil', 123456789, 55),
                   ('Olivia', 'City of Brazil', 123456789, 55),
                   ('Logan', 'City of Brazil', 123456789, 55),
                   ('Evelyn', 'City of Brazil', 123456789, 55),
                   ('Jayden', 'City of Brazil', 123456789, 55),
                   ('Penelope', 'City of Brazil', 123456789, 55),
                   ('Mason', 'City of Brazil', 123456789, 55),
                   ('Madison', 'City of Brazil', 123456789, 55),
                   ('Carter', 'City of Brazil', 123456789, 55),
                   ('Chloe', 'City of Brazil', 123456789, 55);""")
    
    cursor.execute("""INSERT INTO CATEGORY (id_category, category_name) 
                    VALUES 
                    (1, 'Breakfast'),
                    (2, 'Lunch'),
                    (3, 'Snack'),
                    (4, 'Dinner'),
                    (5, 'Drinks'),
                    (6, 'Vegan'),
                    (7, 'Sweet'),
                    (8, 'Appetizers'),
                    (9, 'Seafood'),
                    (10, 'Pasta'),
                    (11, 'Salads'),
                    (12, 'Desserts'),
                    (13, 'Vegetarian'),
                    (14, 'Beverages'),
                    (15, 'Sides'),
                    (16, 'Soup'),
                    (17, 'Entrees'),
                    (18, 'Cocktails'),
                    (19, 'Steak'),
                    (20, 'Burgers'),
                    (21, 'Pizza'),
                    (22, 'Sushi'),
                    (23, 'Tacos'),
                    (24, 'Wraps'),
                    (25, 'Sandwiches'),
                    (26, 'Dim Sum'),
                    (27, 'Wings'),
                    (28, 'Nachos'),
                    (29, 'BBQ'),
                    (30, 'Ribs'),
                    (31, 'Tapas'),
                    (32, 'Fries');""")

    cursor.execute("""INSERT INTO PRODUCT (id_product, product_name, sale_price, category_id_category, status) 
                   VALUES 
                   (1, 'Bread', 1.00, 1, 'Enabled'),
                   (2, 'Roast chicken', 5.20, 2, 'Enabled'),
                   (3, 'Sandwich', 2.30, 3,'Enabled'),
                   (4, 'Noodles', 3.40, 4,'Enabled'),
                   (5, 'Water', 0.25, 5,'Enabled'),
                   (6, 'Tomato and lettuce salad', 2.60, 6,'Enabled'),
                   (7, 'Jam', 3.70, 7,'Enabled'),
                   (8, 'Cheeseburger', 8.50, 20, 'Enabled'),
                   (9, 'Margherita Pizza', 10.99, 21, 'Enabled'),
                   (10, 'California Roll', 12.75, 22, 'Enabled'),
                   (11, 'Beef Tacos', 7.99, 23, 'Enabled'),
                   (12, 'Chicken Wrap', 6.25, 24, 'Enabled'),
                   (13, 'BLT Sandwich', 9.50, 25, 'Enabled'),
                   (14, 'Shrimp Dumplings', 6.99, 26, 'Enabled'),
                   (15, 'Buffalo Wings', 8.99, 27, 'Enabled'),
                   (16, 'Nachos Grande', 10.50, 28, 'Enabled'),
                   (17, 'BBQ Ribs', 14.99, 29, 'Enabled'),
                   (18, 'Prime Rib', 20.75, 19, 'Enabled'),
                   (19, 'Double Cheeseburger', 10.25, 20, 'Enabled'),
                   (20, 'Supreme Pizza', 13.99, 21, 'Enabled'),
                   (21, 'Dragon Roll', 14.75, 22, 'Enabled'),
                   (22, 'Fish Tacos', 9.25, 23, 'Enabled'),
                   (23, 'Turkey Club Wrap', 8.99, 24, 'Enabled'),
                   (24, 'Grilled Cheese Sandwich', 6.50, 25, 'Enabled'),
                   (25, 'Steamed Dumplings', 5.99, 26, 'Enabled'),
                   (26, 'Teriyaki Wings', 9.50, 27, 'Enabled'),
                   (27, 'Loaded Nachos', 11.99, 28, 'Enabled'),
                   (28, 'Honey BBQ Ribs', 16.50, 29, 'Enabled'),
                   (29, 'Filet Mignon', 25.75, 19, 'Enabled'),
                   (30, 'Bacon Cheeseburger', 9.75, 20, 'Enabled'),
                   (31, 'Meat Lovers Pizza', 15.99, 21, 'Enabled'),
                   (32, 'Rainbow Roll', 16.75, 22, 'Enabled');""")
    
    cursor.execute("""INSERT INTO waiter (id_waiter, name, cell_phone) 
                   VALUES 
                   (1, 'Jeferson Santos', 123456789),
                   (2, 'github/devjefersonsantos', 123456789),
                   (3, 'Michael Johnson', 123456789),
                   (4, 'Jennifer Williams', 123456789),
                   (5, 'James Smith', 123456789),
                   (6, 'Lisa Brown', 123456789),
                   (7, 'Robert Jones', 123456789),
                   (8, 'Jessica Davis', 123456789),
                   (9, 'David Miller', 123456789),
                   (10, 'Mary Taylor', 123456789),
                   (11, 'John Anderson', 123456789),
                   (12, 'Lisa Martinez', 123456789),
                   (13, 'Matthew Hernandez', 123456789),
                   (14, 'Jessica Wright', 123456789),
                   (15, 'Daniel Hill', 123456789),
                   (16, 'Susan Scott', 123456789),
                   (17, 'William Green', 123456789),
                   (18, 'Sarah Adams', 123456789),
                   (19, 'Christopher Baker', 123456789),
                   (20, 'Ashley Hall', 123456789),
                   (21, 'Joseph Carter', 123456789),
                   (22, 'Karen Rivera', 123456789),
                   (23, 'Michael Mitchell', 123456789),
                   (24, 'Kimberly Torres', 123456789),
                   (25, 'Christopher Lopez', 123456789),
                   (26, 'Sarah Hill', 123456789),
                   (27, 'Anthony Flores', 123456789),
                   (28, 'Laura King', 123456789),
                   (29, 'Kevin Adams', 123456789),
                   (30, 'Emily Campbell', 123456789),
                   (31, 'Mark Reed', 123456789),
                   (32, 'Melissa Murphy', 123456789);""")
    
    mysql_connection.commit()
    cursor.close()
    mysql_connection.close()

if __name__ == "__main__":
    while True:
        question = input("Are you sure you want to insert fictional data into the database? [Y/N] ")
        if question.upper() == "Y":
            try:
                simulation()
            except Exception as error:
                print(error)
            else:
                print("Data entered successfully.")
                
                logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    filename="log/log.log"
                )
                logging.warning('Fictitious data was added to the database by test file "test_simulation.py"')
            break
        elif question.upper() == "N":
            break
