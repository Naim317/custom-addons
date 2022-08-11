# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class AcademyMain(models.Model):
    _name = 'academy.main'
    _description = 'Academy Main'
    _order = 'admission_year desc, name'

    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Student Email', required=True)
    b_day = fields.Date(string='Birth Date')
    group_members = fields.Many2many('res.partner', string='Group Members')
    group_leader = fields.Char(string='Group Leader')
    group_slogan = fields.Text(string='Group Slogan')
    phone = fields.Char(string='Phone')
    fb_name = fields.Char(string='Facebook Name', required=True)
    fb_link = fields.Char(string='Facebook Profile Link', required=True)
    cgpa = fields.Char(string='CGPA')
    admission_year = fields.Date(string='Admission Year', required=True)
    major_subject = fields.Char(string='Major Subject')
    number_of_awards = fields.Char(string='Number of Awards')
    teacher_remarks = fields.Char(
        [
            ('positive', 'Positive'),
            ('negative', 'Negative')
        ],
        string='Teacher Remarks',
        default=''
    )
    regular_student = fields.Selection(
        [
            ('yes', 'Yes'),
            ('no', 'No')
        ],
        string='Regular Student',
        default=''
    )
    university = fields.Selection(
        [
            ('diu', 'DIU'),
            ('outside_diu', 'Outside-DIU')
        ],
        string='Indexed',
        default='diu'
    )
    fees = fields.Char(string='Fees')
    faculty = fields.Selection(
        [
            ('fsit', 'FSIT'),
            ('fe', 'FE'),
            ('fbe', 'FBE'),
            ('fhss', 'FHSS'),
            ('fahs', 'FAHS')
        ],
        string='Faculty',
        default=''
    )
    department = fields.Selection(
        [
            ('cse', 'CSE'),
            ('swe', 'SWE'),
            ('mct', 'MCT'),
            ('ged', 'GED'),
            ('esdm', 'ESDM'),
            ('cis', 'CIS'),
            ('itm', 'ITM'),
            ('ete', 'ETE'),
            ('te', 'TE'),
            ('eee', 'EEE'),
            ('architecture', 'Architecture'),
            ('ce', 'CE'),
            ('ba', 'BA'),
            ('re', 'RE'),
            ('thm', 'THM'),
            ('i&e', 'I&E'),
            ('english', 'English'),
            ('law', 'Law'),
            ('jmc', 'JMC'),
            ('ds', 'DS'),
            ('pharmacy', 'Pharmacy'),
            ('nfe', 'NFE'),
            ('ph', 'PH')
        ],
        string='Department',
        default=''
    )
    address = fields.Selection(
        [
            ('inside_dhaka', 'Inside-Dhaka'),
            ('outside_dhaka', 'Outside-Dhaka')
        ],
        string='Faculty',
        default=''
    )
    address.inside_dhaka = fields.Selection(
        [
            ('dhanmondi', 'Dhanmondi'),
            ('mirpur', 'Mirpur'),
            ('uttara', 'Uttara'),
            ('mohammadpur', 'Mohammadpur'),
            ('purandhaka', 'Puran Dhaka'),

        ]

    )
    address.outside_dhaka = fields.Selection(
        [
            ('rangpur', 'Rangpur'),
            ('rajshahi', 'Rajshahi'),
            ('mymansing', 'Mymansing'),
            ('chottogram', 'Chottogram'),
            ('khulna', 'Khulna'),
            ('barishal', 'Barishal'),
            ('international', 'International')

        ]

    )

