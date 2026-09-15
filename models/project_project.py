from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    code = fields.Char(string="Project Code")