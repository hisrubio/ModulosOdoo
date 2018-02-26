# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductor(models.Model):
    _name = 'cine.conductor'
    _inherit = 'base.entidad'

    nombre = fields.Char()
    dni = fields.Char()
    #relacion con vehiculos n n