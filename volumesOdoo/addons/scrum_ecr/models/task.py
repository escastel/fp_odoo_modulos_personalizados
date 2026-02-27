# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Task(models.Model):
	_name = 'scrum_ecr.task'
	_description = 'Tarea SCRUM'
	_rec_name = 'name_ecr'
	_order = 'create_date desc'

	name_ecr = fields.Char(string='Nombre', required=True)
	description_ecr = fields.Text(string='Descripción')
	date_end_ecr = fields.Date(string='Fecha de finalización')
	paused_ecr = fields.Boolean(string='En pausa', default=False)
	sprint_id_ecr = fields.Many2one(
        comodel_name='scrum_ecr.sprint',
        string='Sprint',
        ondelete='set null',
    )
	technology_ids_ecr = fields.Many2many(
        comodel_name='scrum_ecr.technology',
        relation='scrum_ecr_task_technology_rel',
        column1='task_id',
        column2='technology_id',
        string='Tecnologías',
    )