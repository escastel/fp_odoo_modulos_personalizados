# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Task(models.Model):
	_name = 'scrum_ecr.task'
	_description = 'Tarea SCRUM'
	_order = 'create_date desc'

	name = fields.Char(string='Nombre', required=True)
	description = fields.Text(string='Descripción')
	create_date = fields.Datetime(string='Fecha de creación', readonly=True)
	date_end = fields.Date(string='Fecha de finalización')
	paused = fields.Boolean(string='En pausa', default=False)