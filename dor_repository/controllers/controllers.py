# -*- coding: utf-8 -*-
# from odoo import http


# class DorRepository(http.Controller):
#     @http.route('/dor_repository/dor_repository', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dor_repository/dor_repository/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dor_repository.listing', {
#             'root': '/dor_repository/dor_repository',
#             'objects': http.request.env['dor_repository.dor_repository'].search([]),
#         })

#     @http.route('/dor_repository/dor_repository/objects/<model("dor_repository.dor_repository"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dor_repository.object', {
#             'object': obj
#         })
