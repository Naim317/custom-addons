# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpiralWorldHigherExpoZone(models.Model):
    _name = 'spiral.world.higher.expo.zone'
    _description = 'SpiralWorld Higher Expo Zone'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Postal Address")
    phone = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    website = fields.Char(string="Company Website")
    video_link = fields.Char(string="Video Link")
    business_type = fields.Char(string="Sector that your business belongs to")

    logo = fields.Binary('Company Logo')
    stall_logo = fields.Binary('Stall Logo')

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')
    document_ids = fields.One2many('spiral.world.higher.expo.document', 'edu_expo_zone_id', string="Document")
    edu_user_ids = fields.One2many('res.users', 'edu_expo_zone_id', string='Counselors')
    edu_chat_ids = fields.One2many('spiral.world.higher.expo.chat', 'edu_expo_zone_id', string='Chat')


class SpiralWorldHigherExpoDocument(models.Model):
    _name = 'spiral.world.higher.expo.document'
    _description = "Spiral World Expo Document"

    name = fields.Char(string="Name", required=True)
    file = fields.Binary(string="File")
    doc_url = fields.Char(string="URL")

    edu_expo_zone_id = fields.Many2one('spiral.world.higher.expo.zone', string='Expo Zone')
    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', related="edu_expo_zone_id.edu_summit_id", string='Summit')


class SpiralWorldExpoChat(models.Model):
    _name = 'spiral.world.higher.expo.chat'
    _description = "Spiral World Expo Chat"

    send_by = fields.Many2one('res.users', string='Send User')
    receive_by = fields.Many2one('res.users', string='Receive User')
    message = fields.Char(string="Message")
    edu_expo_zone_id = fields.Many2one('spiral.world.higher.expo.zone', string='Expo Zone')
    state = fields.Selection([('draft', 'Draft'), ('accept', 'Accept'),('reject', 'Reject')],string="Status", default='draft')

