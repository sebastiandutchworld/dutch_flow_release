from odoo import models, fields, api, tools, _

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    addon_name = fields.Char(string='Addon Name')
    release_id = fields.Many2one('dws.release.management', string='Release')

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
    addon_name = fields.Char(string='Addon Name')
    release_id = fields.Many2one('dws.release.management', string='Release')


class DwsReleaseManagement(models.Model):
    _name = 'dws.release.management'
    _description = 'dws release management'
    
    name = fields.Char(string='Release Number', required=True)
    description = fields.Char(string='Description')
    responsible = fields.Many2one('res.users', string='Responsible', required=True)
    
    deployed = fields.Selection([('no', 'No'), 
                                ('git', 'On Git'), 
                                ('build', 'Build on Jenkins'), 
                                ('test', 'Deployed on test'), 
                                ('prod', 'Deployed on production')],
                                 string='Deployed', required=True)
    
    release_date = fields.Date(string='Release Date', required=True)
    release_line_tasks = fields.Many2many('project.task', 'release_id', string='Release Line Tasks')
    release_line_tickets = fields.Many2many('helpdesk.ticket', 'name', string='Release Line Tickets')    
    customer = fields.Many2one('res.partner', string='Customer', required=True)
    tags = fields.Many2many('project.tags', string='Tags')




