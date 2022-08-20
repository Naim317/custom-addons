from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldExpoWebinar(models.Model):
    _name = 'spiral.world.expo.webinar'
    _description = "Spiral World Webinar"
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    sequence = fields.Integer('Sequence',default='1')
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    banner = fields.Binary(string="Banner")
    summit_id = fields.Many2one('spiral.world.summit', string='Summit')
    speakers_ids = fields.Many2many('spiral.world.expo.webinar.speaker', domain="[('summit_id', '=', summit_id)]", string='Speakers')


class SpiralWorldExpoWebinarSpeaker(models.Model):
    _name = 'spiral.world.expo.webinar.speaker'
    _description = "Spiral World Webinar"
    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer('Sequence',default='1')
    code = fields.Char(string="Code")
    logo = fields.Binary(string="Profile Photo")
    designation = fields.Char(string="Designation")
    company = fields.Char(string="Company")
    summit_id = fields.Many2one('spiral.world.summit', string='Summit')