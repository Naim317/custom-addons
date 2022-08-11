# -*- coding: utf-8 -*-
{
    'name': 'Sir Academy',
    'summary': """All Scopus Publication of DIU""",
    'description': """
DoR Repository
==============
Yearly Scopus indexed publications of DIU faculty will be made available in this module, so that any BERP account holder (faculty members) of DIU will be able to find their individual publications in a particular year      Yearly Scopus indexed publications of DIU faculty will be made available in this module, so that any BERP account holder (faculty members) of DIU will be able to find their individual publications in a particular year.
    """,
    'version': '13.0.1.0',
    'author': 'Nayeem Islam',
    'company': 'Daffodil Software Limited',
    'website': 'https://daffodilsoft.com/',
    'category': 'Tools',
    'sequence': 1,
    'depends': ['base', 'contacts'],
    'data': [
        ## Security
        'security/academy_security.xml',
        'security/ir.model.access.csv',

        ## View
        'views/academy_main_view.xml',
        'views/academy_rules_view.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': "/sir_academy/static/src/img/sir.JPG",
    "images": ["/static/description/banner.png"],
    "license": "OPL-1",
    "price": 0,
    "currency": "EUR",
}
