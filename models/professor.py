#-*- coding: utf-8 -*-

from odoo import models, fields, api


class universityprofessor(models.Model):
    _name = 'university.professor'
    
    f_name = fields.Char('First Name', required=True)
    l_name = fields.Char('Last Name', required=True)
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Sex')
    identity_card = fields.Char('Identity Card', required=True)
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    inscription_date = fields.Datetime('Date of Inscription', default=fields.Datetime.now)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    department_id=fields.Many2one(comodel_name='university.department ')
    subject_id=fields.Many2one(comodel_name='university.subject ')
    classroom_ids=fields.Many2many(comodel_name='university.classroom',
                                   relation='prof_class_rel',
                                   column1='f_name',
                                   column2='name' )
