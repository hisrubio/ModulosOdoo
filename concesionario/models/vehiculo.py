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
    idsconductores=fields.Many2many(string= "conductores",comodel_name='concesionario.conductor',relation = 'rel_conductores_vehiculos',column1='vehiculo', column2='conductor')
    #relacion con viajes uno a muchos
    idsviajes=fields.One2many('concesionario.viaje','idvehiculo',string="viaje")
    #relacion con seguros uno a muchos
    idseguro=fields.Many2one('base.empresa',string="Seguro")

    #campo computado
    fecha_revision = fields.Date(compute="comprobar", store=True)

    @api.onchange('numero_asientos')
    def comprobar(self):
        fechaActual=datetime.now()
        if( self.numero_asientos > 4):
            self.fecha_revision = fechaActual + timedelta(days=1500)
