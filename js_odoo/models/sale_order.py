from odoo import fields, models, api, _
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def generate_data_report(self):

        query = "SELECT * FROM sale_order WHERE state = 'draft'"
        self.env.cr.execute(query)
        line_ids = list(line[0] for line in self.env.cr.fetchall())

        return {
            'type': 'ir.actions.act_window',
            'name': 'Brand Tracking',
            'view_type': 'form',
            'view_mode': 'tree,pivot',
            'res_model': 'sale.order',
            'domain': [('id', 'in', line_ids)],
        }

