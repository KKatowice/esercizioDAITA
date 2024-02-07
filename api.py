from flask import Flask #nome db: museo
app = Flask(__name__)

#--OPERE--
@app.route('/api/getOpere', methods=['GET'])#tutte, maybe parametro per il limit della query
def getWorks():
    pass

@app.route('/api/getOpereByArtist', methods=['GET'])
def getOpereByArtist():
    pass

@app.route('/api/getOpereByDate', methods=['GET'])
def getOpereByDate():
    pass

@app.route('/api/getOpereByTimeSpan', methods=['GET'])
def getOpereByTimeSpan():
    pass

@app.route('/api/getOpereByType', methods=['GET'])
def getOpereByType():
    pass
    
#--ARTISTI--
@app.route('/api/getArtisti', methods=['GET'])#tutti, come getOpere
def getArtisti():
    pass
@app.route('/api/getArtistaByName', methods=['GET'])
def getArtista():
    pass
@app.route('/api/getArtistiByDate', methods=['GET'])#@TODO parametro data morte o nascita
def getOpereByType():
    pass