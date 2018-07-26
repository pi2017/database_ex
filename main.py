import requests
import lxml
import pymongo

client = pymongo.MongoClient()

collection = client.test_db.my_collection

while 1:
    name = input('Введите имя :')
    mail = input("Введите почту :")
    password = input("введите пароль :")
    id = mail

    collection.insert_one({'id': id, "name": name, "email": mail, "password": password})
