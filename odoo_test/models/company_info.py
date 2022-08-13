from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class CompanyInfo(models.Model):
    _name = 'company.info'
    _description = 'Company Info'

    name = fields.Char('Company Name', required=True)
    region = fields.Char('Company Region', required=True)
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attachment = fields.Binary('Attachment')
