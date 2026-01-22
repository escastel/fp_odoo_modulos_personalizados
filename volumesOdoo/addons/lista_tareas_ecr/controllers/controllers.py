# -*- coding: utf-8 -*-
# from odoo import http


# class ListaTareasEcr(http.Controller):
#     @http.route('/lista_tareas_ecr/lista_tareas_ecr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista_tareas_ecr/lista_tareas_ecr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista_tareas_ecr.listing', {
#             'root': '/lista_tareas_ecr/lista_tareas_ecr',
#             'objects': http.request.env['lista_tareas_ecr.lista_tareas_ecr'].search([]),
#         })

#     @http.route('/lista_tareas_ecr/lista_tareas_ecr/objects/<model("lista_tareas_ecr.lista_tareas_ecr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista_tareas_ecr.object', {
#             'object': obj
#         })

