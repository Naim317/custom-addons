from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SpiralWorldSummitResUserInherit(models.Model):
    _inherit = 'res.users'

    user_type = fields.Selection(
        [('draft', 'Draft'), ('visitor', 'Visitor'), ('counselor', 'Counselor'), ('exhibitor', 'Exhibitor'),
         ('organizer', 'Organizer'), ('sponsor', 'Sponsor'), ('judge', 'Judge')], string="User Type", index=True,
        default='draft')
    summit_id = fields.Many2one('spiral.world.summit', string='Summit')
    expo_zone_id = fields.Many2one('spiral.world.expo.zone', string='Expo Zone')
