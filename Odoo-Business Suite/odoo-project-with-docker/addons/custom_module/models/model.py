from odoo import models, fields

class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string='Name', required=True)
    value = fields.Integer(string='Value')
    active = fields.Boolean(string='Active', default=True)