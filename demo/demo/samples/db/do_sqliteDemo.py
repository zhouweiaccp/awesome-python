#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# do-sqliteDemo - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2020/11/19 20:22 https://www.pythoncentral.io/introduction-to-sqlite-in-python/

import sqlite3


# Create a database in RAM
# db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb.db')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE  IF NOT EXISTS  users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()

# Get a cursor object
# cursor = db.cursor()
# cursor.execute('''DROP TABLE users''')
# db.commit()


cursor = db.cursor()
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
print('First user inserted')

# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
print('Second user inserted')
db.commit()

# id = cursor.lastrowid
# print('Last row id: %d' % id)

#  The values of the Python variables are passed inside a tuple. Another way to do this is passing a dictionary using the ":keyname" placeholder:
# cursor.execute('''INSERT INTO users(name, phone, email, password)
#                   VALUES(:name,:phone, :email, :password)''',
#                   {'name':name1, 'phone':phone1, 'email':email1, 'password':password1})
#
# users = [(name1,phone1, email1, password1),
#          (name2,phone2, email2, password2),
#          (name3,phone3, email3, password3)]
# cursor.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)
# db.commit()


#
# cursor.execute('''SELECT name, email, phone FROM users''')
# user1 = cursor.fetchone() #retrieve the first row
# print(user1[0]) #Print the first column retrieved(user's name)
# all_rows = cursor.fetchall()
# for row in all_rows:
#     # row[0] returns the first column in the query (name), row[1] returns email column.
#     print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))


#
# cursor.execute('''SELECT name, email, phone FROM users''')
# for row in cursor:
#     # row[0] returns the first column in the query (name), row[1] returns email column.
#     print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

#
# user_id = 3
# cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id,))
# user = cursor.fetchone()

#
# # Update user with id 1
# newphone = '3113093164'
# userid = 1
# cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
#                (newphone, userid))
#
# # Delete user with id 2
# delete_userid = 2
# cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
#
# db.commit()



#
# cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
#  (newphone, userid))
# db.commit() #Commit the change

#
# cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
#  (newphone, userid))
# db.commit() #Commit the change

# # The user's phone is not updated
# db.rollback()



#
# import sqlite3 #Import the SQLite3 module
# try:
#     # Creates or opens a file called mydb with a SQLite3 DB
#     db = sqlite3.connect('data/mydb')
#     # Get a cursor object
#     cursor = db.cursor()
#     # Check if table users does not exist and create it
#     cursor.execute('''CREATE TABLE IF NOT EXISTS
#                       users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
#     # Commit the change
#     db.commit()
# # Catch the exception
# except Exception as e:
#     # Roll back any change if something goes wrong
#     db.rollback()
#     raise e
# finally:
#     # Close the db connection
#     db.close()


#
# SQLite Row Factory and Data Types
# The following table shows the relation between SQLite datatypes and Python datatypes:
#
# None type is converted to NULL
# int type is converted to INTEGER
# float type is converted to REAL
# str type is converted to TEXT
# bytes type is converted to BLOB
# The row factory class sqlite3.Row is used to access the columns of a query by name instead of by index:
#
# db = sqlite3.connect('data/mydb')
# db.row_factory = sqlite3.Row
# cursor = db.cursor()
# cursor.execute('''SELECT name, email, phone FROM users''')
# for row in cursor:
#     # row['name'] returns the name column in the query, row['email'] returns email column.
#     print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))
# db.close()