# Importamos SQLAlchemy desde flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import datetime

# Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

# Creamos la tabla de Alumnos pasandole el modelo de la db
class Prueba_DBS(db.Model):
    __tablename__ = 'Prueba_dbs'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(70))
    correo = db.Column(db.String(70))
    sueldo = db.Column(db.String(10))
       