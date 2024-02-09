import pandas as pd
from ..dbUtils import *

connection = create_db_connection("museo")
df = pd.read_csv(r"../datasetLeo/dati_artisti_opere.csv")
df['movementLabel'] = df['movementLabel'].fillna('sconosciuto')
df['artistDeathDate'] = df['artistDeathDate'].fillna('sconosciuto')
df['artistBirthDate'] = df['artistBirthDate'].fillna('sconosciuto')


def replace_http(value):
    if isinstance(value, str) and value.startswith('http'):
        return 'sconosciuto'
    else:
        return value

df['artistLabel'] = df['artistLabel'].apply(replace_http)
df['artistBirthDate'] = df['artistBirthDate'].apply(replace_http)

df.drop_duplicates(subset='artistLabel', inplace=True)


set_artisti = set()

q1 = """INSERT INTO artisti(nome, movimento, data_nascita, data_morte)
        VALUES(%s, %s, %s, %s)"""

for e in df.itertuples():
    set_artisti.add((e[4],e[10],e[7],e[8]))

lista_artisti = list(set_artisti)

execute_many_query(connection, q1, lista_artisti)


lista_opere = []
lista_creazione = []

c = 1
for e in df.itertuples():
    lista_opere.append((e[2], e[6], e[5]))
    a = read_query(connection, f"SELECT id_artista FROM artisti WHERE nome = '{e[4]}'")
    if a:
        lista_creazione.append((a[0][0], c))
        c +=1

q2 = """INSERT INTO opere (titolo, data_pubblicazione, url_immagine)
        VALUES (%s, %s, %s)"""

execute_many_query(connection,q2,lista_opere)

q3 = """INSERT INTO creazione (id_artista, id_opera) VALUES (%s, %s)"""

execute_many_query(connection,q3, lista_creazione)