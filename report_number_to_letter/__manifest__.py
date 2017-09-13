# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Monto en letras - Reporte Facturas',
    'summary': 'Este módulo convierte el monto total de una factura a texto (En el reporte QWeb)',
    'version': '10.0.1.0.0',
    'category': 'tools',
    'website': 'https://odootips.com',
    'author': 'OdooTips',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'account',
        'report',
    ],
    'data': [
        'views/res_currency_view.xml',
        'views/report_invoice.xml',
    ],
}
