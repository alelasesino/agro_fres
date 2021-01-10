
from odoo import models, fields


class Parcel(models.Model):
    _name = 'agro.farm.parcel'
    _description = 'Modelo de parcela'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
    number = fields.Char(string='Número', required=True)
    farm_id = fields.Many2one('agro.farm', 'Finca', ondelete='cascade', required=True)
    parcel_line_ids = fields.One2many('agro.farm.parcel.line', 'parcel_id', string='Plantas')
    is_editable = fields.Boolean(default=True, store=False)


class ParcelLine(models.Model):
    _name = 'agro.farm.parcel.line'
    _description = 'Modelo de linea de parcela'
    #_rec_name = 'name'

    parcel_id = fields.Many2one('agro.farm.parcel', 'Parcela', required=True)
    plant_id = fields.Many2one('agro.plant', 'Planta', required=True)
    quantity = fields.Integer('Cantidad')
