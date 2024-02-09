from funzioni_sql import *

connection = create_server_connection("localhost", "corsoUser", "asdasd")
create_database(connection, "CREATE DATABASE museo")
connection = create_db_connection("localhost", "corsoUser", "asdasd", "museo")

artisti = """CREATE TABLE artisti(
            id_artista int PRIMARY KEY AUTO_INCREMENT,
            nome varchar(255) NOT NULL,
            nazionalita varchar(255),
            data_nascita int,
            data_morte int);"""
opere = """CREATE TABLE opere(
            id_opera int PRIMARY KEY AUTO_INCREMENT,
            titolo varchar(255) NOT NULL,
            data_pubblicazione int,
            url_immagine varchar(255));"""
creazione = """CREATE TABLE creazione(
                id int PRIMARY KEY AUTO_INCREMENT,
                id_artista int NOT NULL,
                id_opera int NOT NULL,
                FOREIGN KEY (id_artista) REFERENCES artisti(id_artista),
                FOREIGN KEY (id_opera) REFERENCES opere(id_opera));"""

execute_query(connection, artisti)
execute_query(connection, opere)
execute_query(connection, creazione)

#PROVA
