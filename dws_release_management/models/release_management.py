from odoo import models, fields, api, tools, _

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    addon_name = fields.Many2one('dws.addon', string='Addon Name')
    release_id = fields.Many2one('dws.release.management', string='Release')

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
    addon_name = fields.Many2one('dws.addon', string='Addon Name')
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
    
    expected_release_date = fields.Date(string='Expected Release Date', required=True)
    release_date = fields.Date(string='Release Date')
    release_line_tasks = fields.Many2many('project.task', 'release_id', string='Release Line Tasks', compute='_compute_release_line_tasks')
    release_line_tickets = fields.Many2many('helpdesk.ticket', 'name', string='Release Line Tickets', compute='_compute_release_line_tickets')    
    customer = fields.Many2one('res.partner', string='Customer', required=True)
    tags = fields.Many2many('project.tags', string='Tags')


    # method that iterates through existing tasks and adds them to the release line tasks
    def _compute_release_line_tasks(self):
        for rec in self:
            rec.release_line_tasks = self.env['project.task'].search([('release_id', '=', rec.id)])


    def _compute_release_line_tickets(self):
        for rec in self:
            rec.release_line_tickets = self.env['helpdesk.ticket'].search([('release_id', '=', rec.id)])

class DwsAddon(models.Model):
    _name = 'dws.addon'
    _description = 'dws addon'
    
    name = fields.Char(string='Addon Name', required=True)
    description = fields.Char(string='Description')
    customer = fields.Many2one('res.partner', string='Customer', required=True)
        




