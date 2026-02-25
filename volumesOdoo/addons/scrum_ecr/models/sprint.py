from odoo import models, fields, api

class Sprint(models.Model):
	_name = 'scrum_ecr.sprint'
	_description = 'Sprint SCRUM'
	_order = 'date_start_ecr desc'

	name_ecr = fields.Char(string='Nombre', required=True)
	description_ecr = fields.Text(string='Descripción')
	date_start_ecr = fields.Date(string='Fecha de inicio', required=True)
	date_end_ecr = fields.Date(string='Fecha de finalización', required=True)
	task_ids_ecr = fields.One2many(
        comodel_name='scrum_ecr.task',
        inverse_name='sprint_id_ecr',
        string='Tareas',
    )