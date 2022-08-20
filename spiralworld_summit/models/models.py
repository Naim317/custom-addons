# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class spiralworld_summit(models.Model):
#     _name = 'spiralworld_summit.spiralworld_summit'
#     _description = 'spiralworld_summit.spiralworld_summit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
