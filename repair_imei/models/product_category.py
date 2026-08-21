from odoo import fields,models,api
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = "product.category"

    imei_required = fields.Boolean(
        string="IMEI Required",
        help='Enforce IMEI assignment for all products under this category.'
    )