from flask import Flask, render_template
from api import apiBlueprint
app = Flask(__name__)
app.register_blueprint(apiBlueprint)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/artisti')
def artisti():
   return render_template('pittori.html')

@app.route('/aggiungiArtista')
def aggiungiArtista():
   return render_template('aggiungi_pittore.html')

@app.route('/opere')
def opere():
   return render_template('opere.html')


if __name__ == '__main__':
   app.run(debug=True) 
