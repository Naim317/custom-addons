# -*- coding: utf-8 -*-
# from odoo import http


# class FgsEvent(http.Controller):
#     @http.route('/fgs_event/fgs_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fgs_event/fgs_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fgs_event.listing', {
#             'root': '/fgs_event/fgs_event',
#             'objects': http.request.env['fgs_event.fgs_event'].search([]),
#         })

#     @http.route('/fgs_event/fgs_event/objects/<model("fgs_event.fgs_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fgs_event.object', {
#             'object': obj
#         })
