from flask import Flask, render_template
from api import apiBlueprint
app = Flask(__name__)
app.register_blueprint(apiBlueprint)

@app.route('/')
def home():
   return render_template('index.html')



if __name__ == '__main__':
   app.run(debug=True) 
