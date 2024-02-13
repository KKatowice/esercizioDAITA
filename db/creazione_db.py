from dbUtils import *

connection = create_server_connection()
create_database(connection, "CREATE DATABASE museo")
connection = create_db_connection("museo")

artisti = """CREATE TABLE artisti(
            id_artista int PRIMARY KEY AUTO_INCREMENT,
            nome varchar(255) UNIQUE NOT NULL,
            movimento varchar(255),
            data_nascita datetime,
            data_morte datetime);"""
opere = """CREATE TABLE opere(
            id_opera int PRIMARY KEY AUTO_INCREMENT,
            titolo varchar(255) NOT NULL,
            data_pubblicazione datetime,
            url_immagine varchar(255));"""
creazione = """CREATE TABLE creazione(
                id int PRIMARY KEY AUTO_INCREMENT,
                id_artista int NOT NULL,
                id_opera int NOT NULL,
                FOREIGN KEY (id_artista) REFERENCES artisti(id_artista) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (id_opera) REFERENCES opere(id_opera) ON DELETE CASCADE ON UPDATE CASCADE);"""

execute_query(connection, artisti)
execute_query(connection, opere)
execute_query(connection, creazione)
