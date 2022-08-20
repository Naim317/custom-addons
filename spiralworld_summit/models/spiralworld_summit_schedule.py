from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldSummitSchedule(models.Model):
    _name = 'spiral.world.summit.schedule'
    _description = "Spiral World Summit Schedule"

    name = fields.Char(string="Name", required=True)
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    banner = fields.Binary(string="Banner")
    status = fields.Char(string="Status")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')
    meeting_id = fields.Many2one('spiral.world.summit.meeting', string='Meeting')
    expo_zone_ids = fields.Many2many('spiral.world.expo.zone', domain="[('summit_id', '=', summit_id)]", string='Expo')
