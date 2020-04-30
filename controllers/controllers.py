# -*- coding: utf-8 -*-
#from odoo import http
#import json

#class Webservice(http.Controller):
#    @http.route('/api', auth='public')
#    def index(self, **kw):

        #bom.mapped('name'):

#        product_id = 3

        #bom = http.request.env['product.product'].search([])
        #for product in bom:
        #    print(product.id, product.name, product.free_qty)
        
#        stocks = http.request.env['stock.quant'].search([('product_id', '=', product_id), ('location_id.id', '=', '8')])
#        for stock in stocks:
#            print(stock.location_id.display_name, stock.location_id.id, stock.product_id.name, stock.lot_id.name, stock.inventory_quantity, stock.quantity)


        #return json.dumps(Product)
#        return "hola"

#     @http.route('/webservice/webservice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('webservice.listing', {
#             'root': '/webservice/webservice',
#             'objects': http.request.env['webservice.webservice'].search([]),
#         })

#     @http.route('/webservice/webservice/objects/<model("webservice.webservice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('webservice.object', {
#             'object': obj
#         })
