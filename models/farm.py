
from odoo import models, fields, api

class Farm(models.Model):
    _name = 'agro.farm'
    _description = 'Modelo de finca'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
    code = fields.Char(string='Referencia Interna', required=True)
    partner_id = fields.Many2one('res.partner', 'Compañia', required=True)
    parcel_ids = fields.One2many('agro.farm.parcel', 'farm_id', string='Parcelas', auto_join=True)

    @api.depends('name', 'code')
    def name_get(self):
        # Devuelve el formato que tendrá el nombre de la finca, 
        # el formato establecido es ['code'] 'name'
        res = []
        for field in self:
            res.append((field.id, f'[{field.code}] {field.name}'))
        return res
