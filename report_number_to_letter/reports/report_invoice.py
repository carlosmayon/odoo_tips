# -*- coding: utf-8 -*-
# Copyright 2017, OdooTips

import number_to_letter
from odoo import models, api


class AccountReportInvoice(models.AbstractModel):
    _name = 'report.account.report_invoice'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('account.report_invoice')
        docs = self.env[report.model].browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'data': data,
            'to_word': number_to_letter.to_word,
        }
        return report_obj.render('account.report_invoice', docargs)
