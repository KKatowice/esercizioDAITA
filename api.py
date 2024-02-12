""" 
DATABASE: museo
TABELLE:
    - artisti:
        - id_artista
        - nome
        - nazionalita
        - data_nascita
        - data_morte
    - opere:
        - id_opera
        - titolo
        - data_pubblicazione
        - url_immagine
    - creazione:
        - id
        - id_artista
        - id_opera
 """

from flask import Blueprint,request #nome db: museo
from dbUtils import *

apiBlueprint = Blueprint("apiBlueprint",__name__)
dbname = 'museo'

#--OPERE--
@apiBlueprint.route('/api/getOpere', methods=['GET'])
def getWorks():
    l = request.args.get("limit", default="20")
    if type(l) != int:
        try:
            l = int(l)
        except:
            raise ValueError("Limit must be an integer")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere LIMIT {l};"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getOpereByArtist', methods=['GET'])
def getOpereByArtist(n):
    if not n:
        n = request.args.get("name", type=str)
    print(n,type(n), "in api")
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    #q = f"SELECT * FROM artisti WHERE autore = '{n}';" #join creazione
    q = f"""
    SELECT * FROM opere JOIN creazione JOIN artisti 
    ON artisti.id_artista = creazione.id_artista AND creazione.id_opera = opere.id_opera
    WHERE nome = '{n}';"""
    res = read_query(c,q)
    c.close()
    return res
    

@apiBlueprint.route('/api/getOpereByDate', methods=['GET'])
def getOpereByDate():
    y = request.args.get("year")
    if type(y) != int or type(y) != str or len(str(y)) < 3:
        raise ValueError("Year must be a 3/4-digit integer/string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere WHERE YEAR(data_pubblicazione) = '{y}';"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getOpereByTimeSpan', methods=['GET']) 
def getOpereByTimeSpan():
    s = request.args.get("start", type=str)
    e = request.args.get("end", type=str)
    if type(s) != int or type(s) != str or len(str(s)) < 3:
        raise ValueError("Year[start] must be a 3/4-digit integer/string")
    if type(e) != int or type(e) != str or len(str(e)) < 3:
        raise ValueError("Year[end] must be a 3/4-digit integer/string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM opere WHERE YEAR(data_pubblicazione) BETWEEN '{s}' AND '{e}';"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getOpereUrl', methods=['GET'])
def getOpereUrl():
    t = request.args.get("limit", default="20")
    if type(t) != int:
        try:
            t = int(t)
        except:
            raise ValueError("Limit must be an integer")
    c = create_db_connection(dbname)
    q = f"SELECT url_immagine FROM opere LIMIT {t};"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getOpereUrl_byName', methods=['GET'])
def getOpereUrl_byName():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q = f"SELECT url_immagine FROM opere WHERE titolo = '{n}';"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getOpereUrl_byAuthor', methods=['GET'])
def getOpereUrl_byAuthor():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q=f"""SELECT url_immagine FROM opere JOIN creazione JOIN artisti 
		ON artisti.id_artista = creazione.id_artista AND creazione.id_opera = opere.id_opera
		WHERE nome = '{n}';"""
    res = read_query(c,q)
    c.close()
    return res

    

#--ARTISTI--
@apiBlueprint.route('/api/getArtisti', methods=['GET'])
def getArtisti():
    l = request.args.get("limit", default="20")
    if type(l) != int:
        try:
            l = int(l)
        except:
            raise ValueError("Limit must be an integer")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM artisti LIMIT {l};"
    res = read_query(c,q)
    c.close()
    return res

@apiBlueprint.route('/api/getArtistaByName', methods=['GET'])
def getArtista():
    n = request.args.get("name", type=str)
    if type(n) != str:
        raise ValueError("Name must be a string")
    c = create_db_connection(dbname)
    q = f"SELECT * FROM artisti WHERE nome = '{n}';"
    res = read_query(c,q)
    c.close()
    return res


@apiBlueprint.route('/api/getArtistiByDate', methods=['GET'])
def getOpereByType():
    bod = request.args.get("bornOrDeath", default="born", type=str)
    d = request.args.get("date", type=str)
    if type(d) != int or type(d) != str or len(str(d)) < 3:
        raise ValueError("Year must be a 3/4-digit integer/string")
    if bod != "born" and bod != "death":
        raise ValueError("bornOrDeath must be 'born' or 'death'")
    c = create_db_connection(dbname)
    if bod == "born":
        q = f"SELECT * FROM artisti WHERE YEAR(data_nascita) = '{d}';"
    else:
        q = f"SELECT * FROM artisti WHERE YEAR(data_morte) = '{d}';"
    res = read_query(c,q)
    c.close()
    return res



#--CRUD--
#datetime formato pe date: 'YYYY-MM-DD HH:MM:SS'

@apiBlueprint.route('/api/addArtista', methods=['POST'])
def addArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"INSERT INTO artisti (nome,movimento,data_nascita,data_morte) VALUES ('{data['autore']}','{data['movimento']}','{data['data_di_nascita']}','{data['data_di_morte']}');"
    execute_query(c,q)
    c.close()


@apiBlueprint.route('/api/addOpera', methods=['POST'])
def addOpera():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"INSERT INTO opere (titolo,data_pubblicazione) VALUES ('{data['quadro']}','{data['data_pubblicazione']}');"
    execute_query(c,q)
    q2 = f"SELECT id_artista FROM artisti WHERE nome = '{data['autore']}';"
    id_artista = read_query(c,q2)[0][0]
    q3 = "SELECT id_opera FROM opere ORDER BY id_opera DESC LIMIT 1;"
    id_opera = read_query(c, q3)[0][0]
    q4 = f"INSERT INTO creazione(id_artista, id_opera) VALUES ('{id_artista}', '{id_opera}';"
    execute_query(c, q4)
    c.close()
#TODO: add creazione


@apiBlueprint.route('/api/updateArtista', methods=['PUT'])
def updateArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"UPDATE artisti SET nazionalita = '{data['nazionalita']}', data_nascita = '{data['data_nascita']}', data_morte = '{data['data_morte']}' WHERE nome = '{data['nome']}';"
    execute_query(c,q)
    c.close()

@apiBlueprint.route('/api/updateOpera', methods=['PUT'])
def updateOpera():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"UPDATE opere SET data_pubblicazione = '{data['data_pubblicazione']}', url_immagine = '{data['url_immagine']}' WHERE titolo = '{data['titolo']}';"
    execute_query(c,q)
    c.close()

@apiBlueprint.route('/api/deleteArtista', methods=['DELETE'])
def deleteArtista():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"DELETE FROM artisti WHERE nome = '{data['nome']}';"
    execute_query(c,q)
    c.close()

@apiBlueprint.route('/api/deleteOpera', methods=['DELETE'])
def deleteOpera():
    data = request.get_json()
    c = create_db_connection(dbname)
    q = f"DELETE FROM opere WHERE titolo = '{data['titolo']}';"
    execute_query(c,q)
    c.close()
