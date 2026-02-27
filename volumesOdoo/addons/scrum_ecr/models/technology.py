from odoo import models, fields, api

class Technology(models.Model):
	_name = 'scrum_ecr.technology'
	_description = 'Tecnología SCRUM'
	_rec_name = 'name_ecr'
	_order = 'name_ecr'

	name_ecr = fields.Char(string='Nombre', required=True)
	description_ecr = fields.Text(string='Descripción')
	image_ecr = fields.Image(string='Foto', max_width=200, max_height=200)
	task_ids_ecr = fields.Many2many(
        comodel_name='scrum_ecr.task',
        relation='scrum_ecr_task_technology_rel',
        column1='technology_id',
        column2='task_id',
        string='Tareas',
    )