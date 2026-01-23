# -*- coding: utf-8 -*-
# from odoo import http


# class ScrumEcr(http.Controller):
#     @http.route('/scrum_ecr/scrum_ecr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scrum_ecr/scrum_ecr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('scrum_ecr.listing', {
#             'root': '/scrum_ecr/scrum_ecr',
#             'objects': http.request.env['scrum_ecr.scrum_ecr'].search([]),
#         })

#     @http.route('/scrum_ecr/scrum_ecr/objects/<model("scrum_ecr.scrum_ecr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scrum_ecr.object', {
#             'object': obj
#         })

