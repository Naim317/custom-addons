# -*- coding: utf-8 -*-
{
    'name': 'Faculty of GS Events',
    'summary': """This is a demo project for practice purpose""",
    'description': """
Faculty of GS Events
==============
Yearly Scopus indexed publications of DIU faculty will be made available in this module, so that any BERP account holder (faculty members) of DIU will be able to find their individual publications in a particular year      Yearly Scopus indexed publications of DIU faculty will be made available in this module, so that any BERP account holder (faculty members) of DIU will be able to find their individual publications in a particular year.
    """,
    'version': '13.0.1.0',
    'author': 'Md. Jannat-UL-Naim',
    'company': 'Daffodil Software Limited',
    'website': 'https://daffodilsoft.com/',
    'category': 'Tools',
    'sequence': 1,
    'depends': ['base', 'contacts'],
    'data': [
        ## Security
        'security/event_security.xml',
        'security/ir.model.access.csv',

        ## View
        'views/event_details_view.xml',
        'views/event_participants_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': "/fgs_event/static/description/icon.png",
    "images": ["/static/description/banner.png"],
    "license": "OPL-1",
    "price": 0,
    "currency": "USD",
}
