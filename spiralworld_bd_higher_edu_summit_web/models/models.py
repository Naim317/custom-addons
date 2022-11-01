# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class spiralworld_bd_higher_edu_summit_web(models.Model):
#     _name = 'spiralworld_bd_higher_edu_summit_web.spiralworld_bd_higher_edu_summit_web'
#     _description = 'spiralworld_bd_higher_edu_summit_web.spiralworld_bd_higher_edu_summit_web'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
