# -*- coding: utf-8 -*-
# from odoo import http


# class SpiralworldSummit(http.Controller):
#     @http.route('/spiralworld_summit/spiralworld_summit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spiralworld_summit/spiralworld_summit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spiralworld_summit.listing', {
#             'root': '/spiralworld_summit/spiralworld_summit',
#             'objects': http.request.env['spiralworld_summit.spiralworld_summit'].search([]),
#         })

#     @http.route('/spiralworld_summit/spiralworld_summit/objects/<model("spiralworld_summit.spiralworld_summit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spiralworld_summit.object', {
#             'object': obj
#         })
