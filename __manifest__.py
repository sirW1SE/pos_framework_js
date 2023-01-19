# -*- coding: utf-8 -*-
{
    'name': 'POS GUI',
    'author': 'sirW1SE',
    'company': 'MUTI',
    'maintainer': 'sirW1SE',
    'description': """ This module allows you to display sale order transactions form, graph, search and pivot view.""",
    'summary': """This module allows you to display sale order transactions form, graph, search and pivot view.""",
    'version': '14.0',
    "license": "",
    "category": "Sales",
    'depends': ['point_of_sale'],
    'demo': [],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
        'static/src/xml/pos_product_button_view.xml'
    ],
    'website': "https://github.com/sirW1SE/pos_framework_js",
    'installable': True,
    'application': True,
    'auto_install': False,
}