from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    project_id = fields.Many2one(
        "project.project",
        string="Project",
    )
    attn_partner_id = fields.Many2one(
        "res.partner",
        string="Attn",
        domain="[('parent_id', '=', partner_id)]",
        help="The specific contact person at the vendor this PO is addressed to.",
    )