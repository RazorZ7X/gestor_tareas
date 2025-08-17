#!/usr/bin/env python3
"""
Gestor de Tareas con Flask
Aplicación completa para gestionar tareas
"""

from flask import Flask, request, redirect, render_template, url_for
import json

# Lista global de tareas
tareas = []
siguiente_id = 1

app = Flask(__name__)

def guardar_datos():
    with open('tareas.json', 'w') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

def cargar_datos():
    global siguiente_id, tareas
    try:
        with open('tareas.json', 'r') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id= data['siguiente_id']
    except FileNotFoundError:
        pass

def agregar_tarea(texto):
    """Agregar una nueva tarea a la lista"""
    global siguiente_id
    tarea = {
        'id': siguiente_id,
        'texto': texto,
        'completada': False
    }
    tareas.append(tarea)
    siguiente_id += 1
    guardar_datos()
    return tarea

def completar_tarea(id):
    """Marcar una tarea como completada"""
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            break
    guardar_datos()
def eliminar_tarea(id):
    """Eliminar una tarea de la lista"""
    global tareas
    tareas = [t for t in tareas if t['id'] != id]

#Cargar datos al iniciar la aplicación
cargar_datos()

@app.route('/')
def index():
    """Ruta principal - Mostrar todas las tareas"""
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: (t['completada'], -t['id']))
    return render_template('index.html', title='Inicio', tareas=tareas_ordenadas)

@app.route('/agregar-tarea', methods=['POST'])
def agregar_tarea_route():
    """Ruta para agregar una nueva tarea"""
    texto = request.form.get('texto')
    if texto and texto.strip():
        agregar_tarea(texto.strip())
    return redirect(url_for('index'))

@app.route('/completar-tarea/<int:id>')
def completar_tarea_route(id):
    """Ruta para marcar una tarea como completada"""
    completar_tarea(id)
    return redirect(url_for('index'))

@app.route('/eliminar-tarea/<int:id>')
def eliminar_tarea_route(id):
    """Ruta para eliminar una tarea"""
    eliminar_tarea(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)