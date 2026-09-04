from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"
    manufacturer_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_manufacturer','=',True)]",
        string="Product Manufacturer",
        help="Device manufacturer or OEM brand (e.g., Apple, Samsung, Xiaomi)",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        domain=[("is_manufacturer", "=", False), ("user_id", "=", False)],
    )
