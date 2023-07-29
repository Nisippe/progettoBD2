from pymongo import MongoClient
# Connessione al server MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleziona il database
db = client['progettoBD2']

# Seleziona la collezione
collection = db['progettoBD2']


'''
CREATE
document = {"campo1": valore1, "campo2": valore2}
collection.insert_one(document)

documents = [{"campo1": valore1, "campo2": valore2}, {"campo1": valore3, "campo2": valore4}]
collection.insert_many(documents)

READ
document = collection.find_one({"campo": valore})

documents = collection.find({"campo": valore})
for document in documents:
    print(document)

UPDATE
filter_query = {"campo": valore}
update_query = {"$set": {"campo_da_aggiornare": nuovo_valore}}
collection.update_one(filter_query, update_query)

collection.update_many(filter_query, update_query)

DELETE
filter_query = {"campo": valore}
collection.delete_one(filter_query)

collection.delete_many(filter_query)
'''
