
from odoo import models, fields


class Plant(models.Model):
    _name = 'agro.plant'
    _description = 'Modelo de planta'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
