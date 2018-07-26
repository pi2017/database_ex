"""
MongoDB
simple code
Author : Oleksii Savchenko
2018

"""

import requests
import lxml
import pymongo

client = pymongo.MongoClient()

collection = client.test_db.my_collection

while 1:
    name = input('Введите имя :')
    mail = input("Введите почту :")
    password = input("Введите пароль :")
    id = mail

    try:
        collection.insert_one({'id': id, "name": name, "email": mail, "password": password})
    except Exception:
        print('Что то пошло не так ')
