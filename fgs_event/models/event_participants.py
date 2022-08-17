# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class EventParticipants(models.Model):
    _name = 'event.participants'
    _description = 'Event Participants'

    name = fields.Char(string='Title', required=True)
    email = fields.Char(string='Email', required=True)
    message = fields.Char(string='Message')
