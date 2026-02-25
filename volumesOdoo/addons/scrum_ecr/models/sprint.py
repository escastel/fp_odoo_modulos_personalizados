from odoo import models, fields, api

class Sprint(models.Model):
	_name = 'scrum_ecr.sprint'
	_description = 'Sprint SCRUM'
	_order = 'date_start desc'

	name = fields.Char(string='Nombre', required=True)
	description = fields.Text(string='Descripción')
	date_start = fields.Date(string='Fecha de inicio', required=True)
	date_end = fields.Date(string='Fecha de finalización', required=True)
	task_ids = fields.One2many(
        comodel_name='scrum_ecr.task',
        inverse_name='sprint_id',
        string='Tareas',
    )