from datetime import datetime

import pytz

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import uuid
import random


class SpiralWorldSummitHigherMeeting(models.Model):
    _name = 'spiral.world.higher.meeting'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Spiral World Higher Edu Meeting"

    READONLY_STATES = {'done': [('readonly', True)], 'cancel': [('readonly', True)]}

    name = fields.Char(string="Name", required=True, states=READONLY_STATES)
    partner_ids = fields.Many2many('res.partner', string='Participants', states=READONLY_STATES)

    banner = fields.Binary(string="Banner")

    start_date = fields.Datetime(string="Start Date", states=READONLY_STATES, default=fields.Datetime.now)
    end_date = fields.Datetime(string="End Date", states=READONLY_STATES, default=fields.Datetime.now)

    domain_url = fields.Char(string='Domain Link')

    meeting_link = fields.Char(string='Meeting Link')
    meeting_code = fields.Char(string='Meeting Code')
    password = fields.Char(string='Meeting Password')
    user_id = fields.Many2one('res.users', string='User', states=READONLY_STATES, required=True, default=lambda self: self.env.user.id)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
    ], string='Meeting Status', index=True, default='draft', states=READONLY_STATES)

    edu_summit_id = fields.Many2one('spiral.world.higher.edu.summit', string='Summit')
    video_call_id = fields.Many2one('acs.video.call', string='Call Meeting')
    edu_expo_zone_ids = fields.Many2many('spiral.world.higher.expo.zone', domain="[('edu_summit_id', '=', edu_summit_id)]", string='Expo')

    counselor_ids = fields.Many2many('res.users', string='Counselors')
    meeting_document_ids = fields.One2many('spiral.world.higher.meeting.document','edu_meeting_id', string='Document')

    @api.model
    def create(self, values):

        video_call = self.env['acs.video.call'].sudo().create({
            'user_id': self.env.uid,
            'subject': values['name'],
            'state': values['state'],
            'date': values['start_date']
        })
        values['video_call_id'] = video_call.id

        if values['domain_url']:
            values['meeting_link'] = values['domain_url'] + '/videocall/' + video_call.meeting_code
        else:
            values['meeting_link'] = video_call.meeting_link

        values['meeting_code'] = video_call.meeting_code
        values['password'] = video_call.password

        return super(SpiralWorldSummitHigherMeeting, self).create(values)

    def write(self, values):
        if values.get('domain_url'):
            values['meeting_link'] = values['domain_url'] + '/videocall/'+ self.video_call_id.meeting_code
        if values.get('start_date'):
            self.video_call_id.date = values['start_date']
        return super(SpiralWorldSummitHigherMeeting, self).write(values)

    def action_draft(self):
        self.state = 'draft'
        self.video_call_id.state = 'draft'

    def action_plan(self):
        self.state = 'planned'
        self.video_call_id.state = 'planned'


    def action_done(self):
        self.state = 'done'
        self.video_call_id.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
        self.video_call_id.state = 'cancel'

    def get_partner_ids(self):
        partner_ids = ''
        for line in self.edu_expo_zone_ids:
            for line_user in line.user_ids:
                partner_ids = ',' + str(line_user.partner_id.id) + partner_ids

        for counselor in self.counselor_ids:
            partner_ids = ',' + str(counselor.partner_id.id) + partner_ids

        return partner_ids


class SpiralWorldEduMeetingDocument(models.Model):
    _name = 'spiral.world.higher.meeting.document'
    _description = "Spiral World Meeting Document"

    name = fields.Char(string="Name")
    file = fields.Binary(string="File")

    user_id = fields.Many2one('res.users', string='User ID')
    edu_meeting_id = fields.Many2one('spiral.world.higher.meeting', string='Meeting ID')
