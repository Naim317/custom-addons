# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class PublicationTrend(models.Model):
    _name = 'publication.trend'
    _description = 'Publication Trends'
    _order = 'publication_year desc, name'

    name = fields.Char(string='Title', required=True)
    abstract = fields.Html(string='Abstract', sanitize=True, strip_style=False)
    keywords = fields.Date(string='Keywords')
    author_ids = fields.Many2many('res.partner', string='Co-Authors')
    first_author = fields.Char(string='First Author')
    researchers = fields.Text(string='Researcher Name with Designation')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    cj_name = fields.Char(string='Conference / Journal Name', required=True)
    cj_link = fields.Char(string='Conference / Journal Link', required=True)
    impact = fields.Char(string='Impact and Practical Application')
    publication_year = fields.Char(string='Publication Year', required=True)
    research_area = fields.Char(string='Research Area')
    published_research_work = fields.Char(string='No of Research Published Paper')
    impact_factor = fields.Char(string='Impact Factor')
    remarks = fields.Char(string='Remarks')
    student_involvement = fields.Selection(
        [
            ('yes', 'Yes'),
            ('no', 'No')
        ],
        string='Student Involvement',
        default=''
    )
    indexed = fields.Selection(
        [
            ('scopus', 'Scopus'),
            ('nonscopus', 'Non-Scopus')
        ],
        string='Indexed',
        default='scopus'
    )
    finance_by = fields.Char(string='Funding')
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
