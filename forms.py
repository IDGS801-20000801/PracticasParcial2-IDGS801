from wtforms import validators
from wtforms import IntegerField, StringField, EmailField, TelField
from wtforms import Form


class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='Value not valid')])
    nombre = StringField(
        'nombre',
        [
            validators.DataRequired(message='The name is required'),
            validators.length(min = 4, max = 80, message='Insert a valid name')
        ]
    )
    direccion = StringField(
        'Direccion',
        [
            validators.DataRequired(message='The address is required'),
            validators.length(min = 4, max = 60, message='Insert a valid address')
        ]
    )
    telefono = StringField('Telefono')
    telefono = StringField(
        'Telefono',
        [
            validators.DataRequired(message="The number is required"),
            validators.length(min = 10, max = 10, message='Insert a valid phone numbah')
        ]
    )
    correo = StringField('Correo Eléctronico')
    correo = StringField(
        'Email',
        [
            validators.DataRequired(message="The e-mail is required"),
            validators.email('Insert a valid e-mail')
        ]
    )
    sueldo = StringField('Sueldo')
    sueldo = StringField(
        'Sueldo',
        [
            validators.DataRequired(message="The sálario is required"),
            validators.length(min = 1, max = 10, message='Insert a valid sálario')
        ]
    )