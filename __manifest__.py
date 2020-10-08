# -*- coding: utf-8 -*-
{
    'name': "Agricultura",

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
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/farm_views.xml',
        'views/parcel_views.xml',
        'views/settings.xml',
        'security/ir.model.access.csv',
    ],
}
