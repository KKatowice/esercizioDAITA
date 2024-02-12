from flask import Flask, render_template, request
from api import apiBlueprint
app = Flask(__name__)
app.register_blueprint(apiBlueprint)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/artisti')
def artisti():
   artisti = getArtisti()
   return render_template('pittori.html', artisti= artisti)

@app.route('/aggiungiArtista')
def aggiungiArtista():
   return render_template('aggiungi_pittore.html')

@app.route('/opere')
def opere():
   opere = getWorks()
   return render_template('opere.html', opere=opere)


if __name__ == '__main__':
   app.run(debug=True) 
