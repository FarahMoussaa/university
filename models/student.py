#-*- coding: utf-8 -*-

from odoo import models, fields, api


class universitystudent(models.Model):
    _name = 'university.student'
    f_name = fields.Char('First Name', required=True)
    l_name = fields.Char('Last Name', required=True)
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Sex')
    identity_card = fields.Char('Identity Card', required=True)
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    registraion_date = fields.Datetime('Date of Inscription', default=fields.Datetime.now)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    department_id=fields.Many2one(comodel_name='university.department ')
    classroom_id=fields.Many2one(comodel_name='university.classroom ')
    #subject_ids=fields.Many2many(related='classroom_id.subject_ids')
   # @api.multi
    def name_get(self):
        result=[]
        for student in self:
            name='[' + student.classroom_id.classroom_name + ']' + student.f_name + ' '+ student.l_name
            result.append((student.id,name))
        return result
    
