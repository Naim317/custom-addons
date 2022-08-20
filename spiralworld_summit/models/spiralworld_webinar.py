from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldWebinar(models.Model):
    _name = 'spiral.world.webinar'
    _description = "Spiral World Webinar"

    name = fields.Char(string="Name", required=True)
    schedule_detail = fields.Text(string="Schedule Detail")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')

    webinar_link_ids = fields.One2many('spiral.world.webinar.link', 'webinar_id', string="Webinar")


class SpiralWorldWebinarLink(models.Model):
    _name = 'spiral.world.webinar.link'
    _description = "Spiral World Webinar Link"
    name = fields.Char(string="Name")
    start_date = fields.Datetime(string="Start Date")
    detail = fields.Text(string="Detail")
    url = fields.Char(string="URL")
    banner = fields.Binary(string="Banner")
    status = fields.Selection([('draft', 'Draft'), ('live', 'Live'), ('archive', 'Archive')],
                             string="Status", index=True, default='draft')

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')
    webinar_id = fields.Many2one('spiral.world.webinar', string='Webinar')
