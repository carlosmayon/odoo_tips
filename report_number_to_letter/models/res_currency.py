# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips

from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    long_name = fields.Char(
        string='Nombre Completo',
    )
