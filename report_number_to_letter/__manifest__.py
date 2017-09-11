# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Report amount total in letters',
    'summary': 'This report ',
    'version': '10.0.1.0.0',
    'category': 'tools',
    'website': 'https://odootips.com',
    'author': 'OdooTips',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'account',
        'report',
    ],
    'data': [
        'report_invoice.xml',
    ],
}