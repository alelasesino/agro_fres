
from odoo import models, fields


class Parcel(models.Model):
    _name = 'agro.farm.parcel'
    _description = 'Modelo de parcela'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
    number = fields.Char(string='Número', required=True)
    farm_id = fields.Many2one('agro.farm', 'Finca', ondelete='cascade', required=True)
    is_editable = fields.Boolean(default=True, store=False)
    variety = fields.Char(string="Variedad")
