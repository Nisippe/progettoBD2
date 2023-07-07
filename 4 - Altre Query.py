from pymongo import MongoClient
# Connessione al server MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleziona il database
db = client['progettoBD2']

# Seleziona la collezione
collection = db['progettoBD2']

result=collection.find().sort("title",1)
for document in result:
    print(document)

'''
ORDER BY
result = collection.find().sort("campo_ordine", 1)

# Itera sui risultati dell'ordinamento ascendente
for document in result:
    print(document)
'''

'''
RICERCA PARAMETRICA
find ma con i parametri che vuole l'utente
'''

