pip install python-dotenv

Poi creare file.env con questa struttura (o con i vostri dati obv) con i dati per connessione mysqsl:

ID = 'root'
PSW = ''
H = 'localhost'





wikidata query service x dataset:
"""SELECT DISTINCT ?painting ?paintingLabel ?artist ?artistLabel ?image ?creationDate ?artistBirthDate ?artistDeathDate ?movement ?movementLabel
WHERE {
  ?painting wdt:P31 wd:Q3305213;    # Quadro
            wdt:P170 ?artist;        # Artista
            wdt:P571 ?creationDate;  # Data di creazione
            wdt:P18 ?image.          # Immagine
            
  OPTIONAL { ?artist wdt:P569 ?artistBirthDate. }  # Data di nascita dell'artista
  OPTIONAL { ?artist wdt:P570 ?artistDeathDate. }  # Data di morte dell'artista
  OPTIONAL { ?painting wdt:P135 ?movement. }      # Movimento artistico
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 500"""
