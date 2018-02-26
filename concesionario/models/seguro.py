# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class seguro(models.Model):
    _name = 'base.empresa'
    _inherit = 'base.empresa'

    fecha_vencimiento = fields.Date()
    #relacion con vehiculos uno a muchos
    idsvehiculos=fields.One2many('concesionario.vehiculo','idseguro',string="vehiculo")
    #hacer el form