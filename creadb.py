import pymongo
from pymongo import MongoClient

#  mi connetto a MongoDB
client = MongoClient('localhost', 27017)

# creo database
db = client.testdb

# creo collection di persone
persone_coll = db.persone

# creo indici in ordine ascendente
persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
# creo indice anche su array computer
persone_coll.create_index([("computer", pymongo.ASCENDING)])


# creo documento
p1 = {"nome":"Stefano", "cognome":"Antonelli","eta":31,
"computer":["asus","apple"]}

# Inserisco documento nel database
result_p1 = persone_coll.insert_one(p1)
print(f"Documento p1 inserito con id: {result_p1.inserted_id}")


# creo documento
p2= {"nome":"Gabriele", "cognome":"Antonelli","eta":25,
"computer":["apple"]}

# Inserisco documento nel database
result_p2 = persone_coll.insert_one(p2)
print(f"Documento p2 inserito con id: {result_p2.inserted_id}")

