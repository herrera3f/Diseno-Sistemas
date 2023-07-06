from flask import Flask, render_template, request , redirect
from conectar import *
from jinja2 import Template
from datetime import datetime
from bson.objectid import ObjectId
app = Flask(__name__, static_url_path='/static')



app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    imagen_url = '/static/large.jpg'
    imagen_url2 = '/static/papasF.png'
    imagen_url3 = '/static/Imagen2.png'
    imagen_url4 = '/static/Imagen3.png'
    favicon_url = '/static/x-icon.png'
    
    db = conexion()

    coleccion = db.hamburguesa.find()
    papas = db.papas.find()
    bebidas = db.bebida.find()

      
   
    return render_template('index.html', hamburguesas = coleccion, papas = papas, bebidas = bebidas, imagen_url = imagen_url, imagen_url2 = imagen_url2, imagen_url3 = imagen_url3, imagen_url4 = imagen_url4, favicon_url = favicon_url)


@app.route('/papas')
def papas():
    imagen_url = '/static/large.jpg'
    imagen_url2 = '/static/papasF.png'
    imagen_url3 = '/static/Imagen2.png'
    imagen_url4 = '/static/Imagen3.png'
    favicon_url = '/static/x-icon.png'
    
    db = conexion()

    coleccion = db.papas.find()

    return render_template('papas.html', papas = coleccion, imagen_url = imagen_url, imagen_url2 = imagen_url2, imagen_url3 = imagen_url3, imagen_url4 = imagen_url4, favicon_url = favicon_url)

@app.route('/bebidas')
def bebidas():
    imagen_url = '/static/large.jpg'
    imagen_url2 = '/static/papasF.png'
    imagen_url3 = '/static/Imagen2.png'
    imagen_url4 = '/static/Imagen3.png'
    favicon_url = '/static/x-icon.png'
    
    db = conexion()

    coleccion = db.bebida.find()

    return render_template('bebidas.html', bebidas = coleccion, imagen_url = imagen_url, imagen_url2 = imagen_url2, imagen_url3 = imagen_url3, imagen_url4 = imagen_url4, favicon_url = favicon_url)

@app.route('/hamburguesas')
def hamburguesas():
    imagen_url = '/static/large.jpg'
    imagen_url2 = '/static/papasF.png'
    imagen_url3 = '/static/Imagen2.png'
    imagen_url4 = '/static/Imagen3.png'
    favicon_url = '/static/x-icon.png'
    
    db = conexion()

    coleccion = db.hamburguesa.find()

    return render_template('hamburguesas.html', hamburguesas = coleccion, imagen_url = imagen_url, imagen_url2 = imagen_url2, imagen_url3 = imagen_url3, imagen_url4 = imagen_url4, favicon_url = favicon_url)




if __name__ == '__main__':
    app.run(debug=True)
