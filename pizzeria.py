from models import Pedido_Tabla
from datetime import datetime
from sqlalchemy import extract

def filtrar_por_semana(fecha_filtro):
    pedidoTodos = Pedido_Tabla.query.all()
    pedidos = []

    for pedido in pedidoTodos:
        dia_semana = pedido.fechaCompra.weekday()
        if int(dia_semana) == int(fecha_filtro):
            pedidos.append(pedido)

    return pedidos

def filtrar_por_mes(mes_filtro):
    mes_obj = datetime.strptime(mes_filtro, '%m')
    pedidos = Pedido_Tabla.query.filter(extract('month', Pedido_Tabla.fechaCompra) == mes_obj.month).all()

    return pedidos


def filtrar_comandas_hoy():
    pedidos = Pedido_Tabla.query.filter_by(fechaCompra=datetime.now().date()).all()

    return pedidos


def obtener_dia(fecha_filtro):
    # Obtener el nombre del día según el número
    dias = [
        'Lunes', 'Martes', 'Miercoles', 
        'Jueves', 'Viernes', 'Sabado', 
        'Domingo'
    ]
    dia = dias[int(fecha_filtro)]
    return dia


def obtener_mes(mes_filtro):
    # Obtener el nombre del mes según el número
    meses = [
        'Enero', 'Febrero', 'Marzo', 
        'Abril', 'Mayo', 'Junio', 
        'Julio', 'Agosto', 'Septiembre', 
        'Octubre', 'Noviembre', 'Diciembre'
    ]
    mes = meses[int(mes_filtro) - 1]
    return mes