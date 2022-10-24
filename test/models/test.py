# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Test(models.Model):
    _name = 'test'
    _description = "Test Table"

    name = fields.Char(string="User Name")
    email = fields.Char(string="Email")
    employeeId = fields.Char(string="Employee Id")
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    designation = fields.Char(string="Designation")