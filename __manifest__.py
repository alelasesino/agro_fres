# -*- coding: utf-8 -*-
{
    'name': "Agro Fres",

    'summary': """
        Modulo orientado a la producción agricola""",

    'description': """
        Permitir gestionar las producciones agricolas
    """,

    'author': "Alejandro",
    'website': "http://www.ieslamarisma.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Agricultura',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/farm_views.xml',
        'views/parcel_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
