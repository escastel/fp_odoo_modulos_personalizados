# -*- coding: utf-8 -*-
{
    'name': "Gestión SCRUM",

    'summary': "Gestión de proyectos con metodología SCRUM",

    'description': """
Módulo para la gestión de proyectos SCRUM
    """,

    'author': "Ester Castellano Ríos",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/security.xml', Para la categoria y grupo de usuarios SCRUM
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'installable': True,
    'application': True,
    'auto_install': False,
}

