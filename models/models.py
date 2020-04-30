# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Farm(models.Model):
    _name = 'agro.farm'
    _description = "Farm model"

    display_name = fields.Char(string="Nombre")
    description = fields.Char(string="Descripción")
    code = fields.Integer(string="Referencia Interna")
    farm_ids = fields.One2many('agro.farm.parcel', 'farm_id', 'Parcelas')

class Parcel(models.Model):
    _name = 'agro.farm.parcel'
    _description = "Parcel model"

    display_name = fields.Char(string="Nombre")
    description = fields.Char(string="Descripción")
    number = fields.Integer(string="Numero")
    farm_id = fields.Many2one('agro.farm', 'Finca')


# class webservice(models.Model):
#     _name = 'webservice.webservice'
#     _description = 'webservice.webservice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
