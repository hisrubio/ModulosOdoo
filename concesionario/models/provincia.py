# -*- coding: utf-8 -*-

from odoo import models, fields, api

class provincia(models.Model):
    _name = 'concesionario.provincia'

    nombre_provincia = fields.Char()
    
    viajes_origen=fields.One2many('concesionario.viaje','provincia_origen',string="viaje origen")
    viajes_destino=fields.One2many('concesionario.viaje','provincia_origen',string="viaje destino")
