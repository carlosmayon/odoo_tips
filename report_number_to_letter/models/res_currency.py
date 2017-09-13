# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    long_name = fields.Char(
        string='Nombre Completo',
    )
