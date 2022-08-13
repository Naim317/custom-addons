from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class RegistrationPolicy(models.Model):
    _name = 'registration.policy'
    _description = 'Registration Policy'

    name = fields.Char('Policy Title', required=True)
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attachment = fields.Binary('Attachment')
