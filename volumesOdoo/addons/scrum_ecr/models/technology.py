from odoo import models, fields, api

class Technology(models.Model):
	_name = 'scrum_ecr.technology'
	_description = 'Tecnología SCRUM'
	_order = 'name'

	name = fields.Char(string='Nombre', required=True)
	description = fields.Text(string='Descripción')
	image = fields.Image(string='Foto', max_width=200, max_height=200)