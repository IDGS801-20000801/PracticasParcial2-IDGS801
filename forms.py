from wtforms import Form
from wtforms import validators
from wtforms import StringField, EmailField, IntegerField, DecimalField, DateField, RadioField, BooleanField, SelectField, TelField

class EmployeeForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido'), validators.Length(min=4, max=25)])
    correo = EmailField('Email', [validators.DataRequired(message='Ingresa un Correo Valido')])
    telefono = IntegerField('Telefono', [validators.DataRequired(message='El campo es requerido'), validators.NumberRange(min=2, max=10000000000)])
    direccion = StringField('Direccion', [validators.DataRequired(message='El campo es requerido'), validators.Length(min=4, max=200)])
    sueldo = DecimalField('Sueldo', [validators.DataRequired(message='El campo es requerido'), validators.NumberRange(min=0, max=1000000)])


class PedidoForm(Form):
    id = IntegerField('id')
    nombreCliente = StringField(
        'Nombre', 
        [
            validators.DataRequired(message = 'This field is required'), 
            validators.Length(min = 4, max = 100)
        ]
    )
    direccionEnvio = StringField(
        'Direccion', 
        [
            validators.DataRequired(message='This field is required'), 
            validators.Length(min = 15, max = 250)
        ]
    )
    telefono = TelField(
        'Telefono',
        [
            validators.DataRequired(message='This field is required'), 
            validators.NumberRange(min = 10, max = 20)
        ]
    )
    fechaPedido = DateField(
        'FechaPedido', 
        [
            validators.DataRequired(message='This field is required')
        ]
    )
    tamanioPizza = RadioField(
        'Tamanio', 
        choices=[
            ('Chica', 'Chica $40'), 
            ('Mediana', 'Mediana $80'), 
            ('Grande', 'Grande $120')
        ]
    )

    jamon = BooleanField('Jamon $10')
    pina = BooleanField('Piña $10')
    champin = BooleanField('Champiñones $10')
    
    numPizzas = IntegerField(
        'Pizzas', 
        [
            validators.DataRequired(message='This field is required'), 
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    
    total = DecimalField(
        'Total', 
        [
            validators.DataRequired(message = 'This field is required'), 
            validators.NumberRange(min = 0, max = 1000000)
        ],
        render_kw = { 
                     'readonly': True, 
                     'style': 'font-weight: bold; background-color: #f0f0f0;'
                    }
    )
    pizzas = StringField(
        'Pizzas Array', 
        [
            validators.DataRequired(message='This field is required')
        ]
    )

class FiltroForm(Form):
    dia = SelectField(
        'Dia', 
        choices = [
            ('', 'SELECCIONA DIA O NADOTA'),
            ('0', 'Lunes'), 
            ('1', 'Martes'), 
            ('2', 'Miercoles'), 
            ('3', 'Jueves'), 
            ('4', 'Viernes'), 
            ('5', 'Sabado'), 
            ('6', 'Domingo')
        ]
    )
    mes = SelectField(
        'Mes', 
        choices = [
            ('00', 'SELECCIONA MES O NADOTA'),
            ('01', 'Enero'), 
            ('02', 'Febrero'), 
            ('03', 'Marzo'), 
            ('04', 'Abril'), 
            ('05', 'Mayo'), 
            ('06', 'Junio'), 
            ('07', 'Julio'), 
            ('08', 'Agosto'), 
            ('09', 'Septiembre'), 
            ('10', 'Octubre'), 
            ('11', 'Noviembre'), 
            ('12', 'Diciembre')
        ]
    )