from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class EventDetails(models.Model):
    _name = 'event.details'
    _description = 'Event Details'

    name = fields.Char('Event Name', required=True)
    region = fields.Char('Event Region', required=True)
    org = fields.Char('Event Organizer', required=True)
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    start_date = fields.datetime(string='Start Date')
    attachment = fields.Binary('Attachment')
