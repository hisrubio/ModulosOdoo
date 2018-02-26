# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class vehiculo(models.Model):
    _name = 'concesionario.vehiculo'

    marca = fields.Char()
    color = fields.Selection(
        selection=[('bl', 'blanco'), ('gr', 'gris'), ('ng', 'negro')])
    numero_asientos = fields.Integer()
    #relacion con conductores n n 
    #relacion con viajes

    #campo computado
    # fecha_revision = fields.Date(compute="comprobar", store=True)

    # @api.onchange('numero_asientos')
    # def comprobar(self):
    #     fechaActual=datetime.now()
    #     d1 = datetime.strptime("1500", "%d").date()
    #     if(self.numero_asientos>4):
    #         self.fecha_revision = fechaActual.day + d1