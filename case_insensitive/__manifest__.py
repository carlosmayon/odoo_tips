# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips

{
    'name': 'CASE INSENSITIVE',
    'summary': """
        Modulo de ejemplo de restriccion insensible
    """,
    'description': """
        Ejemplo de caso insensible a las mayúsculas y minúsculas, se
        considerará iguales a: demo, DEMO, Demo, DEMo, etc y no
        permitirá guardar.
    """,
    'version': '10.0.1.0.0',
    'category': 'tools',
    'website': 'https://odootips.com',
    'author': 'OdooTips',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'views/demo_view.xml',
    ],
}
