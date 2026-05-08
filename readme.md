# 💄 Makeup vick

**Proyecto Etapa 1 - Backend con APIs**  
**Materia: Programación Web 2 
**Tecnicatura en Tecnologías Web

**Alumno:** Victoria Lezcano 
sede: marcos paz 

---

## Descripción del Proyecto

Este proyecto es una **API RESTful** para una tienda de productos de maquillaje. Incluye un catálogo de productos y un carrito de compras funcional.


---

## pasos cumplidos:

- ✅ Listar productos disponibles (`/api/productos`)
- ✅ Agregar productos al carrito (`/api/agregar/<id>`)
- ✅ Eliminar productos del carrito (`/api/quitar/<id>`)
- ✅ Ver carrito y calcular total (`/api/carrito`)
- ✅ Persistencia en memoria usando sesiones de Flask
- ✅ Documentación completa con Swagger

---

## Tecnologías Utilizadas

- **Python** + **Flask**
- **Flasgger** (para documentación Swagger)
- **Jinja2** (templates HTML)
- **HTML5 + CSS3**
- Sesiones de Flask

---

## 📁 Estructura del Proyecto
tp_parte_1
├── app.py   
|                 # Archivo principal (API + rutas web)
├── templates/
|   |
│   ├── base.html
|   |
│   ├── index.html
|   |
│   ├── carrito.html
|   |
│   └── docs.html
|
├── static/
|   |
│   └── style.css
|
└── README.md


La documentación interactiva de la API está disponible en:
http://127.0.0.1:5000/apidocs