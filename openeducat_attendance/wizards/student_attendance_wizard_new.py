# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentAttendanceWizard(models.TransientModel):
    _name = 'student.attendance.new'

    from_date = fields.Date(
        'From Date')
    to_date = fields.Date(
        'To Date')

    course_id = fields.Many2one('op.course', string="Course")
    batch_id = fields.Many2many('op.batch', string="Batch")
    student_id = fields.Many2many('op.student', string="Student")
    session_id =fields.Many2many('op.session', string="Session")

    @api.multi
    @api.constrains('from_date', 'to_date')
    def check_dates(self):
        for record in self:
            from_date = fields.Date.from_string(record.from_date)
            to_date = fields.Date.from_string(record.to_date)

            if from_date and to_date and to_date < from_date:
                raise ValidationError(
                    _("To Date cannot be set before From Date."))


    # @api.onchange('course_id')
    # def fill_batches(self):
    #     self.batch_id = False
    #     return {'domain': {'batch_id': [('id', '=', self.course_id.id)]}}

    # @api.onchange('batch_id')
    # def fill_sessions(self):
    #     self.session_id = False
    #     return {'domain': {'session_id': [('id', '=', self.batch_id.id)]}}

    # @api.onchange('session_id')
    # def fill_students(self):
    #     self.student_id = False
    #     domain = {}
    #     # data = [(self.env['op.student'].search([]), 'in', 'id' )]
    #     # print(":::::::::::::data::::::::::",len(data))
    #     # if len(data) > 0:
    #     #     domain = {'domain': {'student_id': data}}
    #     # else:
    #     #     domain = {'domain': {'student_id': [(self.batch_id,'in','id')]}}
    #     return {'domain': {'student_id': [('id','=',self.batch_id.id)]}}

    @api.multi
    def print_report(self):
        pass
        # data = self.read(['from_date', 'to_date'])[0]
        # data.update({'student_id': self.env.context.get('active_id', False)})

        # return self.env.ref(
        #     'openeducat_attendance.action_report_student_attendance') \
        #     .report_action(self, data=data)
