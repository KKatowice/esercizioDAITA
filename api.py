from flask import Blueprint,request #nome db: museo

apiBlueprint = Blueprint("apiBlueprint",__name__)

#--OPERE--
@apiBlueprint.route('/api/getOpere', methods=['GET'])
def getWorks(args):
    args.get("limit", default="20", type=str)
    pass

@apiBlueprint.route('/api/getOpereByArtist', methods=['GET'])
def getOpereByArtist(args):
    args.get("name", type=str)
    pass

@apiBlueprint.route('/api/getOpereByDate', methods=['GET'])
def getOpereByDate(args):
    args.get("year", type=str)
    pass

@apiBlueprint.route('/api/getOpereByTimeSpan', methods=['GET']) #parametri: data inizio, data fine
def getOpereByTimeSpan(args):
    args.get("bornOrDeath", default="born", type=str)
    args.get("start", type=str)
    args.get("end", type=str)
    pass

@apiBlueprint.route('/api/getOpereUrl', methods=['GET'])
def getOpereByType(args):
    args.get("limit", default="20", type=str)
    pass

@apiBlueprint.route('/api/getOpereUrl_byName', methods=['GET'])
def getOpereUrl_byName(args):
    args.get("name", type=str)
    pass

@apiBlueprint.route('/api/getOpereUrl_byAuthor', methods=['GET'])
def getOpereUrl_byAuthor(args):
    args.get("name", type=str)
    pass

    

#--ARTISTI--
@apiBlueprint.route('/api/getArtisti', methods=['GET'])
def getArtisti(args):
    args.get("limit", default="20", type=str)
    pass

@apiBlueprint.route('/api/getArtistaByName', methods=['GET'])
def getArtista(args):
    args.get("name", type=str)
    pass

@apiBlueprint.route('/api/getArtistiByDate', methods=['GET'])
def getOpereByType(args):
    args.get("bornOrDeath", default="born", type=str)
    args.get("date", type=str)
    pass



#--CRUD--

@apiBlueprint.route('/api/addArtista', methods=['POST'])
def addArtista(args):
    data = request.get_json()
    pass
@apiBlueprint.route('/api/addOpera', methods=['POST'])
def addOpera(args):
    data = request.get_json()
    pass

@apiBlueprint.route('/api/updateArtista', methods=['PUT'])
def updateArtista(args):
    data = request.get_json()
    pass
@apiBlueprint.route('/api/updateOpera', methods=['PUT'])
def updateOpera(args):
    data = request.get_json()
    pass

@apiBlueprint.route('/api/deleteArtista', methods=['DELETE'])
def deleteArtista(args):
    data = request.get_json()
    pass
@apiBlueprint.route('/api/deleteOpera', methods=['DELETE'])
def deleteOpera(args):
    data = request.get_json()
    pass
