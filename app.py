from flask import Flask, render_template, request
from api import *
app = Flask(__name__)
app.register_blueprint(apiBlueprint)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/pittori')
def artisti():
   artisti = getArtisti()
   return render_template('pittori.html', artisti= artisti)

@app.route('/aggiungiArtista')
def aggiungiArtista():
   return render_template('aggiungi_pittore.html')

@app.route('/quadri')
def opere():
   n = str(request.args.get("nome"))
   print(n, type(n))
   print("vivo")
   if n:
      opere = getOpereByArtist(n)
   else:
      opere = getWorks()
   return render_template('quadri.html', opere=opere)


if __name__ == '__main__':
   app.run(debug=True) 
