from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldExpoZone(models.Model):
    _name = 'spiral.world.expo.zone'
    _description = "Spiral World Expo Zone"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Postal Address")
    phone = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    website = fields.Char(string="Company Website")
    video_link = fields.Char(string="Video Link")
    business_type = fields.Char(string="Sector that your business belongs to")

    logo = fields.Binary('Company Logo')
    stall_logo = fields.Binary('Stall Logo')


    social_media = fields.Char(string="Social Media")
    company_type = fields.Selection([('draft', 'Draft'), ('sponsor', 'Sponsor'), ('participate', 'Participate'), ('organizer', 'Organizer')], string="Company Type", index=True, default='draft')

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')
    country_id = fields.Many2one('spiral.world.country', string='Country')

    summit_schedule_id = fields.Many2one('spiral.world.summit.schedule', string='Schedule')

    user_ids = fields.One2many('res.users', 'expo_zone_id', string='Counselors')
    document_ids = fields.One2many('spiral.world.expo.document', 'expo_zone_id', string="Document")


class SpiralWorldExpoDocument(models.Model):
    _name = 'spiral.world.expo.document'
    _description = "Spiral World Expo Document"

    name = fields.Char(string="Name", required=True)
    file = fields.Binary(string="File")
    doc_url = fields.Char(string="URL")

    expo_zone_id = fields.Many2one('spiral.world.expo.zone', string='Expo Zone')
    summit_id = fields.Many2one('spiral.world.summit', related="expo_zone_id.summit_id", string='Summit')


class SpiralWorldExpoZone_country(models.Model):
    _name = 'spiral.world.country'
    _description = "Spiral World Country"
    name = fields.Char(string="Name", required=True)
    logo = fields.Binary('Company Logo')
    expo_zone_ids = fields.One2many('spiral.world.expo.zone', 'country_id', string="Expo Zone")