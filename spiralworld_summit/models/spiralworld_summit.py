from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldSummit(models.Model):
    _name = 'spiral.world.summit'
    _description = "Spiral World Summit"

    name = fields.Char(string="Name", required=True)
    video_url = fields.Char(string="Video URL")
    live_url = fields.Char(string="Live URL")
    live_image = fields.Binary(string="Live Image")
    zoom_id = fields.Char(string="Zoom ID")
    state = fields.Selection([('draft', 'Draft'), ('process', 'Process'), ('done', 'Done'), ('close', 'Close')],
                             string="Status", index=True, default='draft')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    expo_zone_ids = fields.One2many('spiral.world.expo.zone', 'summit_id', string='Expo')
    webinar_ids = fields.One2many('spiral.world.webinar', 'summit_id', string='Webinar')
    summit_meeting_ids = fields.One2many('spiral.world.summit.meeting', 'summit_id', string='Meeting')
    summit_schedule_ids = fields.One2many('spiral.world.summit.schedule', 'summit_id', string='Schedule')
    summit_webinar_archive_ids = fields.One2many('spiral.world.webinar.archive', 'summit_id', string='Archive')
    summit_photo_ids = fields.One2many('spiral.world.summit.photo', 'summit_id', string='Photo')
    summit_news_ids = fields.One2many('spiral.world.summit.news', 'summit_id', string='News')
    summit_video_ids = fields.One2many('spiral.world.summit.video', 'summit_id', string='Video')

    expo_zone_count = fields.Integer(compute="expo_zones_count", string='Expo Zone Count')
    webinar_count = fields.Integer(compute="webinars_count", string='Webinar Count')
    summit_meeting_count = fields.Integer(compute="summit_meetings_count", string='Meeting Count')
    summit_schedule_count = fields.Integer(compute="summit_schedules_count", string='Meeting Count')

    def expo_zones_count(self):
        for partner in self:
            partner.expo_zone_count = len(partner.expo_zone_ids.search([('summit_id','=',partner.id)]))

    def send_mail(self):
        meeting = self.env['spiral.world.summit.meeting'].sudo().search([('summit_id','=',self.id)])
        print("Start Sent Mail")
        for meet in meeting:
            print(meet.name)
            meet.action_send_invitaion()


    def webinars_count(self):
        for partner in self:
            partner.webinar_count = len(partner.webinar_ids.search([('summit_id','=',partner.id)]))

    def summit_meetings_count(self):
        for partner in self:
            partner.summit_meeting_count = len(partner.summit_meeting_ids.search([('summit_id','=',partner.id)]))

    def summit_schedules_count(self):
        for partner in self:
            partner.summit_schedule_count = len(partner.summit_schedule_ids.search([('summit_id','=',partner.id)]))


class SpiralWorldArchive(models.Model):
    _name = 'spiral.world.webinar.archive'
    _description = "Spiral World Webinar Archive"

    name = fields.Char(string="Name")
    webinar_link = fields.Char(string="Webinar Link")
    date = fields.Date(string="Date")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')


class SpiralWorldSummitPhoto(models.Model):
    _name = 'spiral.world.summit.photo'
    _description = "Photo"

    name = fields.Char(string="Name")
    photo = fields.Binary(string="Photo")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')


class SpiralWorldSummitNews(models.Model):
    _name = 'spiral.world.summit.news'
    _description = "News"

    name = fields.Char(string="Name")
    news = fields.Binary(string="News Image")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')


class SpiralWorldSummitVideo(models.Model):
    _name = 'spiral.world.summit.video'
    _description = "Video"

    name = fields.Char(string="Name")
    video = fields.Char(string="Video")

    summit_id = fields.Many2one('spiral.world.summit', string='Summit')