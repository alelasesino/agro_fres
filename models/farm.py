
from odoo import models, fields, api


class Farm(models.Model):
    _name = 'agro.farm'
    _description = 'Modelo de finca'
    #_rec_name = 'name'

    @api.depends('name', 'code')
    def name_get(self):
        # Devuelve el formato que tendrá el nombre de la finca,
        # el formato establecido es ['code'] 'name'
        res = []
        for field in self:
            res.append((field.id, f'[{field.code}] {field.name}'))
        return res

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
    code = fields.Char(string='Referencia Interna', required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    parcel_ids = fields.One2many('agro.farm.parcel', 'farm_id', string='Parcelas')
