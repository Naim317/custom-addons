# -*- coding: utf-8 -*-
# from odoo import http


# class SirAcademy(http.Controller):
#     @http.route('/sir_academy/sir_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sir_academy/sir_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sir_academy.listing', {
#             'root': '/sir_academy/sir_academy',
#             'objects': http.request.env['sir_academy.sir_academy'].search([]),
#         })

#     @http.route('/sir_academy/sir_academy/objects/<model("sir_academy.sir_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sir_academy.object', {
#             'object': obj
#         })
