# 📋 Gestor de Tareas con Flask

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blueviolet.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Una aplicación web moderna y funcional para gestionar tareas personales y profesionales, desarrollada con Flask, Jinja2 y Bootstrap 5.

## ✨ Características Principales

### 🎯 **Gestión de Tareas**
- ✅ **Crear tareas** con descripción detallada
- ✅ **Marcar como completadas** con un solo clic
- ✅ **Eliminar tareas** con confirmación
- ✅ **IDs incrementales** automáticos
- ✅ **Estado persistente** durante la sesión

### 🎨 **Interfaz de Usuario**
- 🎨 **Diseño moderno** con Bootstrap 5
- 📱 **Completamente responsivo** para móviles y desktop
- 🌈 **Gradientes y animaciones** atractivas
- 🔍 **Búsqueda en tiempo real** de tareas
- 🏷️ **Filtros inteligentes** por estado

### 📊 **Dashboard y Estadísticas**
- 📈 **Contador de tareas totales**
- ⏰ **Tareas pendientes** en tiempo real
- ✅ **Tareas completadas** con porcentaje
- 📊 **Barra de progreso** visual
- 🔄 **Actualización automática** de estadísticas

### 🚀 **Funcionalidades Avanzadas**
- ⚡ **Validación de formularios** HTML5
- 📝 **Contador de caracteres** con indicadores visuales
- 🔍 **Búsqueda inteligente** con filtros
- 🎯 **Ordenamiento automático** (pendientes primero)
- 💾 **Persistencia de datos** en memoria

## 🛠️ Tecnologías Utilizadas

### **Backend**
- **Python 3.8+** - Lenguaje de programación principal
- **Flask 3.0+** - Framework web ligero y flexible
- **Jinja2** - Motor de plantillas integrado

### **Frontend**
- **HTML5** - Estructura semántica moderna
- **CSS3** - Estilos avanzados y animaciones
- **Bootstrap 5.3** - Framework CSS responsivo
- **Font Awesome 6.4** - Iconografía profesional
- **JavaScript ES6+** - Interactividad del lado del cliente

### **Herramientas de Desarrollo**
- **pipenv** - Gestión de dependencias y entorno virtual
- **Git** - Control de versiones

## 📋 Requisitos del Sistema

### **Requisitos Mínimos**
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

### **Requisitos Recomendados**
- Python 3.11+
- 4GB RAM
- Conexión a internet (para CDNs de Bootstrap y Font Awesome)

## 🚀 Instalación y Configuración

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/gestor-tareas.git
cd gestor-tareas
```

### **2. Crear Entorno Virtual**
```bash
# Instalar pipenv si no lo tienes
pip install pipenv

# Crear y activar entorno virtual
pipenv install
pipenv shell
```

### **3. Instalar Dependencias**
```bash
pipenv install
```

### **4. Ejecutar la Aplicación**
```bash
pipenv run python app.py
```

### **5. Acceder a la Aplicación**
Abre tu navegador y ve a: **http://127.0.0.1:5000**

## 📁 Estructura del Proyecto

```
gestor_tareas/
├── app.py                 # Aplicación principal Flask
├── Pipfile               # Configuración de dependencias
├── Pipfile.lock          # Versiones exactas de dependencias
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   └── index.html       # Plantilla principal con Jinja2
└── .gitignore           # Archivos ignorados por Git
```

## 🔧 Configuración y Personalización

### **Variables de Entorno**
```bash
# Puerto de la aplicación (por defecto: 5000)
export FLASK_PORT=5000

# Modo debug (por defecto: True)
export FLASK_DEBUG=True

# Host de la aplicación (por defecto: 0.0.0.0)
export FLASK_HOST=0.0.0.0
```

### **Personalización de Estilos**
Los estilos CSS están integrados en `templates/index.html` y pueden ser modificados directamente:
- Colores del tema
- Tipografías
- Espaciados y márgenes
- Efectos de hover y transiciones

## 📖 Uso de la Aplicación

### **Agregar Nueva Tarea**
1. Escribe la descripción en el campo de texto
2. El contador de caracteres te mostrará el límite (500)
3. Haz clic en "Agregar Tarea"
4. La tarea aparecerá en la lista con estado "Pendiente"

### **Completar Tarea**
1. Busca la tarea en la lista
2. Haz clic en el botón "Completar" (verde)
3. La tarea cambiará a estado "Completada"
4. Se moverá al final de la lista

### **Eliminar Tarea**
1. Localiza la tarea que deseas eliminar
2. Haz clic en el botón de papelera (rojo)
3. Confirma la eliminación en el diálogo
4. La tarea se eliminará permanentemente

### **Búsqueda y Filtrado**
- **Búsqueda**: Escribe en la barra de búsqueda para filtrar por texto
- **Filtros**: Usa los botones "Todas", "Pendientes", "Completadas"
- **Combinación**: Combina búsqueda y filtros para resultados precisos

## 🔌 API Endpoints

La aplicación incluye endpoints RESTful para integración con otros sistemas:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Página principal con lista de tareas |
| `POST` | `/agregar-tarea` | Crear nueva tarea |
| `GET` | `/completar-tarea/<id>` | Marcar tarea como completada |
| `GET` | `/eliminar-tarea/<id>` | Eliminar tarea por ID |

## 🧪 Pruebas y Desarrollo

### **Ejecutar en Modo Desarrollo**
```bash
pipenv run python app.py
```

### **Características de Desarrollo**
- ✅ **Auto-reload** al modificar archivos
- 🐛 **Modo debug** activado
- 📍 **PIN del debugger** mostrado en consola
- 🔄 **Recarga automática** del servidor

### **Logs y Debugging**
- Los logs se muestran en la consola
- Errores detallados en modo debug
- Trazabilidad completa de requests

## 🚀 Despliegue en Producción

### **Configuración de Producción**
```bash
# Deshabilitar modo debug
export FLASK_DEBUG=False

# Configurar servidor WSGI
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### **Servidor WSGI Recomendado**
- **Gunicorn** para Linux/Unix
- **Waitress** para Windows
- **uWSGI** para alta concurrencia

### **Variables de Entorno de Producción**
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
export FLASK_SECRET_KEY=tu-clave-secreta-aqui
```

## 🤝 Contribuir al Proyecto

### **Cómo Contribuir**
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### **Estándares de Código**
- Seguir PEP 8 para Python
- Usar nombres descriptivos para variables y funciones
- Documentar funciones con docstrings
- Mantener el código limpio y legible

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre** - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- **Flask Team** por el excelente framework web
- **Bootstrap Team** por el framework CSS
- **Font Awesome** por los iconos profesionales
- **Comunidad Python** por el soporte continuo

## 📞 Soporte

Si tienes preguntas o problemas:

- 📧 **Email**: tu-email@ejemplo.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/tu-usuario/gestor-tareas/issues)
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/tu-usuario/gestor-tareas/discussions)

## 🔄 Historial de Versiones

### **v1.0.0** - Versión Inicial
- ✅ Gestión básica de tareas (CRUD)
- ✅ Interfaz web moderna con Bootstrap 5
- ✅ Dashboard con estadísticas
- ✅ Búsqueda y filtrado
- ✅ Validación de formularios
- ✅ Sistema de rutas RESTful

---

⭐ **Si este proyecto te ha sido útil, ¡dale una estrella en GitHub!**
