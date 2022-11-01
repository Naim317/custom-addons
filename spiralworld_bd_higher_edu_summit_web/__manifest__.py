# -*- coding: utf-8 -*-
{
    'name': "spiralworld_bd_higher_edu_summit_web",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Md. Mahfuzur Rahman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/templates_participating_details.xml',
        'views/templates_participating_institute.xml',
        'views/templates_sponsor.xml',
        'views/templates_suvenior.xml',
        'views/templates_speaker.xml',
        'views/templates_home_chief_guest.xml',
        'views/templates_home_about.xml',
        'views/templates_slider.xml',
        'views/templates_menu.xml',
        'views/templates_login.xml',
        'views/templates_master.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
