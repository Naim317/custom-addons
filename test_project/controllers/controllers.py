# -*- coding: utf-8 -*-
# from odoo import http


# class TestProject(http.Controller):
#     @http.route('/test_project/test_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_project/test_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_project.listing', {
#             'root': '/test_project/test_project',
#             'objects': http.request.env['test_project.test_project'].search([]),
#         })

#     @http.route('/test_project/test_project/objects/<model("test_project.test_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_project.object', {
#             'object': obj
#         })
