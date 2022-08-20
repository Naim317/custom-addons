# -*- coding: utf-8 -*-
{
    'name': "B2B Summit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'demo/demo.xml',
        'views/spiralworld_speaker.xml',
        'views/spiralworld_country.xml',
        'views/spiralworld_summit_schedule.xml',
        'views/spiralworld_webinar_link.xml',
        'views/spiralworld_webinar.xml',
        'views/spiralworld_expo_document.xml',
        'views/spiralworld_expo_zone.xml',
        'views/spiralworld_summit_meeting.xml',
        'views/spiralworld_summit.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
