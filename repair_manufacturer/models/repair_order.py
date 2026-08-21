from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class RepairOrder(models.Model):
    _inherit="repair.order"
    manufacturer_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_manufacturer','=',True)]",
        string="Product Manufacturer",
        help= "Device manufacturer or OEM brand (e.g., Apple, Samsung, Xiaomi)"
    )