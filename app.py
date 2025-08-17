#!/usr/bin/env python3
"""
Esqueleto de Aplicación Flask Simple
Aplicación mínima con Hola Mundo
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    """Ruta principal - Hola Mundo"""
    return '<h1>¡Hola Mundo!</h1><p>Bienvenido a Flask</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
