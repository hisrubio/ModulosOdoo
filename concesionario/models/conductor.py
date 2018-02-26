# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductor(models.Model):
    _name = 'concesionario.conductor'
    _inherit = 'base.entidad'

    nombre = fields.Char()
    dni = fields.Char()
    #relacion con vehiculos n n
    idsvehiculos=fields.Many2many(string= "vehiculos",comodel_name='concesionario.vehiculo',relation = 'rel_conductores_vehiculos',column1='conductor', column2='vehiculo')
