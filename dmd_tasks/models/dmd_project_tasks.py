# -*- coding: utf-8 -*-

# import xmlrpc.client
# from datetime import datetime
from odoo import models, fields, api, exceptions


class ProjectTask(models.Model):
    # _inherit = ['mail.thread', 'mail.activity.mixin']  # error if stay in next row
    _inherit = 'project.task'

    date_start = fields.Date(string='Date start')
    date_stop = fields.Date(string='Date stop')

    ref_id = fields.Many2one('project.task', string='Parent task', ondelete='restrict', index=True)
    task_dependency_ids = fields.One2many('project.task', 'ref_id', string='Arrow from tasks')
    # task_dependency_ids = fields.Many2many('project.task', string='Arrow from tasks')  # error
