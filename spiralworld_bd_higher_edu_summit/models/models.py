# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class spiralworld_bd_higher_edu_summit(models.Model):
#     _name = 'spiralworld_bd_higher_edu_summit.spiralworld_bd_higher_edu_summit'
#     _description = 'spiralworld_bd_higher_edu_summit.spiralworld_bd_higher_edu_summit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
