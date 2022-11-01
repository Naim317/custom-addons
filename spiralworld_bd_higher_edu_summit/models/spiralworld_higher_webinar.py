from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldHigherWebinar(models.Model):
    _name = 'spiral.world.higher.webinar'
    _description = "Spiral World Webinar"

    name = fields.Char(string="Name", required=True)
    schedule_detail = fields.Text(string="Schedule Detail")

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')

    edu_webinar_link_ids = fields.One2many('spiral.world.higher.webinar.link', 'edu_webinar_id', string="Webinar")


class SpiralWorldWebinarLink(models.Model):
    _name = 'spiral.world.higher.webinar.link'
    _description = "Spiral World Webinar Link"
    name = fields.Char(string="Name")
    start_date = fields.Datetime(string="Start Date")
    detail = fields.Text(string="Detail")
    url = fields.Char(string="URL")
    banner = fields.Binary(string="Banner")
    status = fields.Selection([('draft', 'Draft'), ('live', 'Live'), ('archive', 'Archive')], string="Status", index=True, default='draft')

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')
    edu_webinar_id = fields.Many2one('spiral.world.higher.webinar', string='Webinar')
