# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas_ecr(models.Model):
     #Nombre y descripcion del modelo de datos
     _name = 'lista_tareas_ecr.lista_tareas_ecr'
     _description = 'lista_tareas_ecr.lista_tareas_ecr'

	#Elementos de cada fila del modelo de datos
     tarea = fields.Char()
     prioridad = fields.Integer()
     urgente = fields.Float(compute="_value_urgente", store=True)
     realizada = fields.Boolean(string="¿Realizada?", default=False)
     fecha_limite = fields.Date(string="Fecha Límite")

	#Este cómputo depende de la variable prioridad
     @api.depends('prioridad')
     #Función para calcular el valor de urgente
     def _value_urgente(self):
         for record in self:
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False


