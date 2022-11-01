# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpiralWorldHigherEduSummit(models.Model):
    _name = 'spiral.world.higher.edu.summit'
    _description = 'SpiralWorld Higher Edu Summit'

    name = fields.Char(string="Name", required=True)
    video_url = fields.Char(string="Video URL")
    live_url = fields.Char(string="Live URL")
    live_image = fields.Binary(string="Live Image")
    zoom_id = fields.Char(string="Zoom ID")
    state = fields.Selection([('draft', 'Draft'), ('process', 'Process'), ('done', 'Done'), ('close', 'Close')],
                             string="Status", index=True, default='draft')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    edu_expo_zone_ids = fields.One2many('spiral.world.higher.expo.zone', 'edu_summit_id', string='Expo')
    edu_archive_ids = fields.One2many('spiral.world.higher.archive', 'edu_summit_id', string='Archive')
    edu_photo_ids = fields.One2many('spiral.world.higher.photo', 'edu_summit_id', string='Photo')
    edu_webinar_ids = fields.One2many('spiral.world.higher.webinar', 'edu_summit_id', string='Webinar')
    edu_news_ids = fields.One2many('spiral.world.higher.news', 'edu_summit_id', string='News')
    edu_video_ids = fields.One2many('spiral.world.higher.video', 'edu_summit_id', string='Videos')
    edu_summit_meeting_ids = fields.One2many('spiral.world.higher.meeting', 'edu_summit_id', string='Meeting')

    edu_expo_zone_count = fields.Integer(compute="edu_expo_zones_count", string='Expo Zone Count')
    edu_archive_count = fields.Integer(compute="edu_archives_count", string='Archive Count')
    edu_photo_count = fields.Integer(compute="edu_photos_count", string='Photo Count')
    edu_webinar_count = fields.Integer(compute="edu_webinars_count", string='Webinar Count')
    edu_summit_meeting_count = fields.Integer(compute="edu_summit_meetings_count", string='Meeting Count')

    def edu_expo_zones_count(self):
        for partner in self:
            partner.edu_expo_zone_count = len(partner.edu_expo_zone_ids.search([('edu_summit_id','=',partner.id)]))

    def edu_archives_count(self):
        for partner in self:
            partner.edu_archive_count = len(partner.edu_archive_ids.search([('edu_summit_id','=',partner.id)]))

    def edu_webinars_count(self):
        for partner in self:
            partner.edu_webinar_count = len(partner.edu_webinar_ids.search([('edu_summit_id','=',partner.id)]))

    def edu_summit_meetings_count(self):
        for partner in self:
            partner.edu_summit_meeting_count = len(partner.edu_summit_meeting_ids.search([('edu_summit_id','=',partner.id)]))


class SpiralWorldHigherEduArchive(models.Model):
    _name = 'spiral.world.higher.archive'
    _description = "Spiral World Higher Archive"

    name = fields.Char(string="Name")
    webinar_link = fields.Char(string="Webinar Link")
    date = fields.Date(string="Date")

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')


class SpiralWorldHigherEduPhoto(models.Model):
    _name = 'spiral.world.higher.photo'
    _description = "Photo"

    name = fields.Char(string="Name")
    photo = fields.Binary(string="Photo")

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')


class SpiralWorldHigherEduNews(models.Model):
    _name = 'spiral.world.higher.news'
    _description = "News"

    name = fields.Char(string="Name")
    news = fields.Binary(string="News Image")

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')


class SpiralWorldHigherEduVideo(models.Model):
    _name = 'spiral.world.higher.video'
    _description = "Video"

    name = fields.Char(string="Name")
    video = fields.Char(string="Video")

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')
