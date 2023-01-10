# -*- coding: utf-8 -*-
#BY: LUIS FELIPE PATERNINA VITAL
from odoo import models, fields, _

class Courses(models.Model):

    _name = "courses"
    _description = "Courses"

    name = fields.Char(string='Name of the subject', required=True, tracking=True)
    credit_number = fields.Integer(string="Credit Numbers")
    teacher_id = fields.Many2one('teachers',string="Teacher in charge")
    area_ids = fields.Many2many('area', string="Related areas")
    area_id_custom = fields.Char(string="Areas", compute="_get_areas")


    @api.model
    @api.depends('area_ids')
    def _get_areas(self):
        for rec in self:
            if rec.area_ids:
                area_custom = ','.join([p.name for p in rec.area_ids])
                rec.area_id_custom = area_custom
            else:
                rec.area_id_custom = ''
