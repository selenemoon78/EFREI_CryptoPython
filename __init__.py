from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/jack')
def jack():
    return render_template('jack.html')

@app.route('/chenille')
def chenille():
    return render_template('chenille.html')

@app.route('/svg')
def svg():
    return render_template('svg.html')
  
@app.route('/maison')
def maison():
    return render_template('maison.html')


@app.route('/exercice1')
def exercice_1():
    return render_template('exercice1.html')

@app.route('/exercice2')
def exercice_2():
    return render_template('exercice2.html')

@app.route('/exercice3')
def exercice_3():
    return render_template('exercice3.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
