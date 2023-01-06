from odoo import fields, models, api, _
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'
