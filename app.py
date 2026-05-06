from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'Makeup_vick_secret_key_2026'

# ==================== PRODUCTOS DE MAQUILLAJE ====================
productos = [
    {"id": 1, "nombre": "Base Líquida Matte", "descripcion": "Cobertura media-alta, duración 12hs", "precio": 8500},
    {"id": 2, "nombre": "Corrector Full Coverage", "descripcion": "Alta cobertura, anti ojeras", "precio": 6200},
    {"id": 3, "nombre": "Paleta de Sombras 12 Tonos", "descripcion": "Tonos neutros y vibrantes", "precio": 12400},
    {"id": 4, "nombre": "Máscara de Pestañas Volumen", "descripcion": "Efecto pestañas postizas", "precio": 4900},
    {"id": 5, "nombre": "Labial Mate Líquido", "descripcion": "Fórmula vegana, larga duración", "precio": 5200},
    {"id": 6, "nombre": "Rubor en Polvo", "descripcion": "Acabado natural, varios tonos", "precio": 4800},
    {"id": 7, "nombre": "Iluminador Glow", "descripcion": "Efecto iluminado radiante", "precio": 6700},
    {"id": 8, "nombre": "Delineador Líquido Negro", "descripcion": "Precisión extrema, a prueba de agua", "precio": 4300},
    {"id": 9, "nombre": "Primer Facial", "descripcion": "Fija el maquillaje y minimiza poros", "precio": 7800},
    {"id": 10, "nombre": "Set de Brochas Pro", "descripcion": "10 brochas profesionales", "precio": 15900},
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)


@app.route('/agregar/<int:id>')
def agregar(id):
    if 'carrito' not in session:
        session['carrito'] = []
    
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        item = next((item for item in session['carrito'] if item['id'] == id), None)
        if item:
            item['cantidad'] += 1
        else:
            session['carrito'].append({
                'id': producto['id'],
                'nombre': producto['nombre'],
                'precio': producto['precio'],
                'cantidad': 1
            })
        flash(f'✓ {producto["nombre"]} agregado al carrito 💄', 'success')
    
    return redirect(url_for('index'))


@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)


@app.route('/quitar/<int:id>')
def quitar(id):
    if 'carrito' in session:
        session['carrito'] = [item for item in session['carrito'] if item['id'] != id]
    return redirect(url_for('carrito'))


@app.route('/vaciar')
def vaciar():
    session.pop('carrito', None)
    flash('Carrito vaciado 🗑️', 'info')
    return redirect(url_for('carrito'))


if __name__ == '__main__':
    app.run(debug=True)