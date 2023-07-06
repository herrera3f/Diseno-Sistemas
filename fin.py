from conectar import *

db = conexion()
coleccion = db.hamburguesa

documentos = coleccion.find()

for documentos in documentos:
    print(documentos)