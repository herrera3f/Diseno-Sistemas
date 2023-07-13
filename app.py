from flask import Flask, render_template, request , redirect, session
from conectar import *
from jinja2 import Template
from datetime import datetime
from bson.objectid import ObjectId
import os
app = Flask(__name__, static_url_path='/static')





app = Flask(__name__)
app.secret_key = os.urandom(24)

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

      
   
    return render_template('index.html', hamburguesas = coleccion, papas = papas, bebidas = bebidas, imagen_url = imagen_url, imagen_url2 = imagen_url2, imagen_url3 = imagen_url3, imagen_url4 = imagen_url4, favicon_url = favicon_url,)


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

# Ruta para mostrar el carrito
# Ruta para mostrar el carrito
@app.route('/carrito')
def mostrar_carrito():
    db = conexion()
    
    carrito_ids = session.get('carrito', [])
    carrito = []

    for producto_id in carrito_ids:
        producto = db.productos.find_one({"_id": ObjectId(producto_id)})
        if producto:
            carrito.append(producto)

    return render_template('carrito.html', carrito=carrito)



# Rutas para agregar productos al carrito
@app.route('/agregar_hamburguesa/<hamburguesa_id>')
def agregar_hamburguesa(hamburguesa_id):
    db = conexion()
    producto = db.hamburguesa.find_one({"_id": ObjectId(hamburguesa_id)})
    if producto:
        session.setdefault('carrito', []).append(str(hamburguesa_id))

    return redirect('/carrito')



@app.route('/agregar_bebida/<bebida_id>')
def agregar_bebida(bebida_id):
    db = conexion()
    producto = db.bebida.find_one({"_id": ObjectId(bebida_id)})
    if producto:
        session.setdefault('carrito', []).append(str(bebida_id))

    return redirect('/carrito')

@app.route('/agregar_papas/<papas_id>')
def agregar_papas(papas_id):
    db = conexion()
    producto = db.papas.find_one({"_id": ObjectId(papas_id)})
    if producto:
        session.setdefault('carrito', []).append(str(papas_id))

    return redirect('/carrito')



if __name__ == '__main__':
    app.run(debug=True)
