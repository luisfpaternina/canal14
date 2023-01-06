from odoo import fields, models, api, _
from datetime import datetime
import logging
from odoo.exceptions import ValidationError


class WizardSaleOrder(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "sale order wizard"

    date = fields.Date(
        string="Date")
