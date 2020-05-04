# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Farm(models.Model):
    _name = 'agro.farm'
    _description = 'Modelo de finca'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    code = fields.Char(string='Referencia Interna')
    parcel_ids = fields.One2many('agro.farm.parcel', 'farm_id', string='Parcelas', auto_join=True)

    @api.depends('name', 'code')
    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, f'[{field.code}] {field.name}'))
        return res

class Parcel(models.Model):
    _name = 'agro.farm.parcel'
    _description = 'Modelo de parcela'
    #_rec_name = 'name'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    number = fields.Char(string='Número')
    farm_id = fields.Many2one('agro.farm', 'Finca', ondelete='cascade', auto_join=True)

