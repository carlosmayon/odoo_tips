# flake8:noqa
# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips

from odoo import models, fields, api
from odoo.exceptions import Warning


class DemoModel(models.Model):
    _name = 'demo.model'

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    @api.constrains('name')
    def _check_name_insensitive(self):
        model_ids = self.search([('id', '!=', self.id)])
        list_names = [x.name.upper() for x in model_ids if x.name]
        if self.name.upper() in list_names:
            raise Warning(
                "ya existe un registro con el nombre: %s " % (self.name.upper())
            )
