# -*- coding: utf-8 -*-
# from odoo import http


# class SpiralworldBdHigherEduSummit(http.Controller):
#     @http.route('/spiralworld_bd_higher_edu_summit/spiralworld_bd_higher_edu_summit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spiralworld_bd_higher_edu_summit/spiralworld_bd_higher_edu_summit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spiralworld_bd_higher_edu_summit.listing', {
#             'root': '/spiralworld_bd_higher_edu_summit/spiralworld_bd_higher_edu_summit',
#             'objects': http.request.env['spiralworld_bd_higher_edu_summit.spiralworld_bd_higher_edu_summit'].search([]),
#         })

#     @http.route('/spiralworld_bd_higher_edu_summit/spiralworld_bd_higher_edu_summit/objects/<model("spiralworld_bd_higher_edu_summit.spiralworld_bd_higher_edu_summit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spiralworld_bd_higher_edu_summit.object', {
#             'object': obj
#         })
