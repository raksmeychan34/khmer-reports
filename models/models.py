# from odoo import models, fields, api


# class khmer_reports(models.Model):
#     _name = 'khmer_reports.khmer_reports'
#     _description = 'khmer_reports.khmer_reports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

