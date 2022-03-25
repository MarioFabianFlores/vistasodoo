
from odoo import api, fields, models


class EscMaterias(models.Model):
    _name = 'esc.materias'
    _description = 'modelo de las materias'

    @api.depends('attendees_ids')
    def computerAttendees(self):
        self.attendees_number= 5*5

    name = fields.Char(string="Nombre",required=True)
    duration=fields.Integer(string="Duración",required=True)
    start_date= fields.Date(string="Fecha De Inicio",required=True)
    end_date= fields.Date(string="Fecha De Termino",required=True)
    code=fields.Char(string="Código",required=True)
    attendees_number=fields.Integer (string="Número De Asistente",compute='computerAttendees')
    attendees_ids=fields.One2many('esc.alumnos','couses_id',string="ID Asistente",required=True)
    teacher_id=fields.Many2one('res.users',string="Maestro")
    school_id=fields.Many2one('esc.escuelas',string="Escuela")
    color=fields.Integer()
