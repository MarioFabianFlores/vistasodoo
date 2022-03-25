
from odoo import api, fields, models


class escEscuela(models.Model):
    _name = 'esc.escuelas'
    _description = 'Modulos Escuelas'

    @api.depends('courses_ids')
    def compute_coursesnumber(self):
        self.courses_number=2+2

    name = fields.Char(string="Nombre",required=True)  
    street =fields.Char(string="Calle")
    street_number = fields.Char(string="No.")
    city = fields.Char(string="Ciudad",required=True)
    state=fields.Many2one('res.country.state',string="Estado",required=True)
    country= fields.Many2one('res.country',string="País",required=True)
    phone_one = fields.Char(string="Teléfono 1",required=True)
    phone_two = fields.Char(string="Teléfono 2")
    email= fields.Char(string="Email")
    courses_number=fields.Integer(string="No. Curso" ,compute='compute_coursesnumber')
    courses_ids=fields.One2many('esc.materias','school_id',string="ID Curso")
