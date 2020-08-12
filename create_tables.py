import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_users_table = " CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT ) "

cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY,name TEXT,price REAL,store_id INTEGER)"

cursor.execute(create_items_table)

create_stores_table = "CREATE TABLE IF NOT EXISTS stores(id INTEGER PRIMART KEY ,name TEXT)"

cursor.execute(create_stores_table)

connection.commit()

connection.close()
