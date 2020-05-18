
from odoo import models, fields, api

class AgroSettings(models.TransientModel):
    _inherit = "res.config.settings"


    partner_id = fields.Many2one('res.partner')
    location_id = fields.Many2one('stock.location', domain="[('usage', '=', 'internal')]")


    def _default_partner_id(self):
        partner = self.env['res.partner'].search([])
        return partner[0].id


    def _default_location_id(self):
        location = self.env['stock.location'].search([('usage', '=', 'internal')])
        return location[0].id


    @api.model
    def get_values(self):
        res = super(AgroSettings, self).get_values()
        ir_config = self.env['ir.config_parameter'].sudo()

        partner_id = ir_config.get_param('agro_fres.partner_id', default=self._default_partner_id())
        location_id = ir_config.get_param('agro_fres.location_id', default=self._default_location_id())

        res.update(partner_id=int(partner_id), location_id=int(location_id))

        return res


    def set_values(self):
        super(AgroSettings, self).set_values()

        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param('agro_fres.partner_id', self.partner_id.id)
        ir_config.set_param('agro_fres.location_id', self.location_id.id)

