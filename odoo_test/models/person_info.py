# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class PersonInfo(models.Model):
    _name = 'person.info'
    _description = 'Person Info'

    name = fields.Char(string='Title', required=True)
    email = fields.Char(string='Email', required=True)
    message = fields.Char(string='Message')
