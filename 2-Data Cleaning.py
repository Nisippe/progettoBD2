from pymongo import MongoClient

# Connessione al server MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleziona il database
db = client['progettoBD2']

# Seleziona la collezione
collection = db['progettoBD2']

# Utilizza l'aggregazione per rimuovere documenti duplicati
pipeline = [
    {"$group": {"_id": {"title": "$title"}, "duplicates": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}
]

# Esegui l'aggregazione per trovare i duplicati
result = collection.aggregate(pipeline)

# Lista per memorizzare gli ID dei documenti duplicati
duplicate_ids = []

# Itera sui risultati dell'aggregazione
for doc in result:
    duplicate_ids.extend(doc['duplicates'])

# Rimuovi i documenti duplicati
collection.delete_many({"_id": {"$in": duplicate_ids}})

filter_query={"position": "none"}
result=collection.delete_many(filter_query)
print(f"numero di righe eliminate: {result.deleted_count}")
