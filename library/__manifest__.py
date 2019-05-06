# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """Modul per a gestionar una llibreria""",

    'description': """Modul per a gestionar una llibreria M10""",

    'author': "Alex Romero",
    'website': "http://www.romero.com",

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
        'views/book_view.xml',
        'views/category_view.xml',
        'views/author_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}