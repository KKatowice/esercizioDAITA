import pandas as pd
from dbUtils import *
import datetime
import re


def mainInsert():
    connection = create_db_connection("museo")
    df = pd.read_csv(r"datasetLeo/dati_artisti_opere.csv")
    df['movementLabel'] = df['movementLabel'].fillna('sconosciuto')
    placeh = str(datetime.datetime.now()).split(" ")[0]
    df['artistDeathDate'] = df['artistDeathDate'].fillna(placeh)
    df['artistBirthDate'] = df['artistBirthDate'].fillna(placeh)
    #print(placeh)

    def replace_http(value):
        if isinstance(value, str) and value.startswith('http'):
            return 'sconosciuto'
        else:
            return value
        
    def replace_httpDate(value):
        if isinstance(value, str) and value.startswith('http'):
            return placeh
        else:
            print(value)
            rgx = r"\b[1-9]\d{3}-\d{2}-\d{2}T"
            print(value, value, bool(re.search(rgx,value)))
            if bool(re.search(rgx,value)):
                return value.split("T")[0]


    df['artistLabel'] = df['artistLabel'].apply(replace_http)
    df['artistBirthDate'] = df['artistBirthDate'].apply(replace_httpDate)
    df['artistDeathDate']  = df['artistDeathDate'].apply(replace_httpDate)
    #print(df.head)
    df['creationDate']  = df['creationDate'].apply(replace_httpDate)
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
        a = read_query(connection, f"""SELECT id_artista FROM artisti WHERE nome = "{e[4]}";""")
        if a:
            #print(a)
            lista_creazione.append((a[0]['id_artista'], c))
            c +=1

    q2 = """INSERT INTO opere (titolo, data_pubblicazione, url_immagine)
            VALUES (%s, %s, %s)"""

    execute_many_query(connection,q2,lista_opere)

    q3 = """INSERT INTO creazione (id_artista, id_opera) VALUES (%s, %s)"""

    execute_many_query(connection,q3, lista_creazione)