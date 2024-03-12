from flask import Flask, render_template, request, Response
from forms import EmployeeForm, PedidoForm, FiltroForm
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import redirect
from models import db
from models import Empleados, Detalle_Pizza, Pedido_Tabla
import json
from pizzeria import filtrar_por_mes, filtrar_por_semana, filtrar_comandas_hoy, obtener_dia, obtener_mes
from sqlalchemy import extract

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'),404

@app.route("/empleados", methods=["GET", "POST"])
def index():
    emp_form = EmployeeForm(request.form)
    if request.method == 'POST':
        emp = Empleados(nombre = emp_form.nombre.data,
                        correo = emp_form.correo.data,
                        telefono = emp_form.telefono.data,
                        direccion = emp_form.direccion.data,
                        sueldo = emp_form.sueldo.data)

        db.session.add(emp)
        db.session.commit()

    return render_template(
        "empleados.html", 
        form = emp_form
    )

@app.route("/tablaEmpleados", methods=["GET", "POST"])
def ABC_Completo():
    empleados = Empleados.query.all()
    return render_template(
        "tablaEmpleados.html", 
        empleados = empleados
    )

@app.route("/pizzeria")
def pizzeria():
    filtro_form = FiltroForm(request.form)
    fecha_filtro = request.args.get('dia')
    mes_filtro = request.args.get('mes')
    ventas = 0.0
    filtro = ''

    if fecha_filtro:
        pedidos = filtrar_por_semana(fecha_filtro)
        filtro = 'Dia: ' + obtener_dia(fecha_filtro)

    elif mes_filtro and mes_filtro != '00':
        pedidos = filtrar_por_mes(mes_filtro)
        filtro = 'Mes: ' + obtener_mes(mes_filtro)

    else:
        pedidos = filtrar_comandas_hoy()
        filtro = 'del Dia de Hoy'

    for pedido in pedidos:
        ventas += pedido.totalCompra

    return render_template(
        "pizzeria.html", 
        pedidos = pedidos, 
        form = filtro_form, 
        ventas = ventas, 
        filtro = filtro
    )

@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    ped_form = PedidoForm(request.form)
    if request.method == 'POST':
        pizzas = ped_form.pizzas.data
        print(pizzas)
        nombre = ped_form.nombreCliente.data
        direccion = ped_form.direccionEnvio.data
        telefono = ped_form.telefono.data
        fecha = ped_form.fechaPedido.data
        print(nombre, direccion, telefono, fecha)

        pizzas_json = json.loads(pizzas)

        encabezado = Pedido_Tabla(
            nombreCliente = ped_form.nombreCliente.data,
            direccionEnvio = ped_form.direccionEnvio.data,
            fechaCompra = ped_form.fechaPedido.data,
            telefono = ped_form.telefono.data,
            totalCompra = ped_form.total.data
        )

        db.session.add(encabezado)
        db.session.commit()

        pedido = Pedido_Tabla.query.order_by(Pedido_Tabla.id_pedido.desc()).first()

        for piz in pizzas_json:
            pizza = Detalle_Pizza(
                tamanioPizza=piz['tamanio'],
                ingredientes="'" + "', '".join(piz['ingredientes']) + "'",
                numPizzas=piz['numPizzas'],
                subtotal=piz['subtotal'],
                id_pedido=pedido.id_pedido
            )

            db.session.add(pizza)
            db.session.commit()

        return redirect('/pizzeria')
    
    elif request.method == 'GET':
        if request.args.get('id'):
            id = request.args.get('id')
            ped1 = db.session.query(Pedido_Tabla).filter_by(id_pedido=id).first() 
            ped_form.nombreCliente.data = ped1.nombreCliente
            ped_form.direccionEnvio.data = ped1.direccionEnvio
            ped_form.telefono.data = ped1.telefono
            ped_form.total.data = ped1.totalCompra
            ped_form.fechaPedido.data = ped1.fechaCompra
            ped_form.id.data = request.args.get('id')
            pizzasDet = db.session.query(Detalle_Pizza).filter_by(id_pedido=id).all()

            pizzas = []
            for piz in pizzasDet:
                pizzas.append({
                    'tamanio': piz.tamanioPizza, 
                    'ingredientes': piz.ingredientes.split("', '"), 
                    'numPizzas': piz.numPizzas, 
                    'subtotal': piz.subtotal
                })

            print(pizzas)
            ped_form.pizzas.data = json.dumps(pizzas)
        
    return render_template(
        "pedido.html", 
        form = ped_form
    )

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()