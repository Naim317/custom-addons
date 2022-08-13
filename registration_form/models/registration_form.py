# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class RegistrationForm(models.Model):
    _name = 'registration.form'
    _description = 'Registration Form'

    name = fields.Char(string='Title', required=True)