import pymongo
from pymongo import MongoClient

#  mi connetto a MongoDB
client = MongoClient('localhost', 27017)

# accesso al database
db = client.testdb

# uso collection persone
persone_coll = db.persone

# cerco il primo oggetto in collezione
p = persone_coll.find_one()
print(p)


print("***")
# trova tutti i documenti nella collection persone che hanno asus come computer
persone = persone_coll.find({"computer":"asus"})

for persona in persone:
    print(persona)

print("***")
#  aggiornare un documento
res = persone_coll.update_one({"nome":"Stefano"}, {"$set": {"eta":32}})
p = persone_coll.find_one({"nome":"Stefano"})
print(p)
