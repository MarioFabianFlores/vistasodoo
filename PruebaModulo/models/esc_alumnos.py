from odoo import api, fields, models


class EscAlumnos(models.Model):
    _name = 'esc.alumnos'
    _description = 'modelo de los alumnos'

    partner_id = fields.Many2one('res.partner',string="Alumno",required=True)
    age= fields.Integer(string="Edad",required=True)
    couses_id=fields.Many2one('esc.materias',string="Cursos")