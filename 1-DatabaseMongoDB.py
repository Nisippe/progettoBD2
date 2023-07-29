'''
# Connessione al server MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleziona il database
db = client['progettoBD2']

# Seleziona la collezione
collection = db['progettoBD2']

# Converte il dataframe pandas in una lista di dizionari
data = df.to_dict(orient='records')

# Inserisci i documenti nel database
collection.insert_many(data)
'''