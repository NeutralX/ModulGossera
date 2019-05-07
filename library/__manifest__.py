# -*- coding: utf-8 -*-
{
    'name': "Protectora d'animals Managment",

    'summary': """Modul per a gestionar una protectora d'animals""",

    'description': """Modul per a gestionar una protectora d'animals""",

    'author': "Alex Romero & Eduard Vila",
    'website': "http://www.romeroandvila.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestió',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/gos_view.xml',
        'views/race_gos_view.xml',
        'views/gat_view.xml',
        'views/race_gat_view.xml',
        'views/inventari_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}