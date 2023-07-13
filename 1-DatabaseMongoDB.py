import pandas as pd
from pymongo import MongoClient

# Carica il dataset in un dataframe pandas
df = pd.read_csv('Top 500 Songs.csv')

# Rimuovi le righe con valori nulli
df.dropna(inplace=True)
df['streak']=df['streak'].str.replace(' weeks','')
df['streak']=df['streak'].str.replace(' week','')
df['position']=df['position'].str.replace('No. ','')
df['position']=df['position'].str.replace('No.','')
df.to_csv("cazzi.csv")
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
collection.insert_many(data)'''