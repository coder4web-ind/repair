from odoo import fields,models,api
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = "product.category"

    imei_required = fields.Selection(
        [
            ("yes","Yes"),
            ("no","No"),
            ("parent","Parent")
        ],
        string="IMEI Required",
        help='Enforce IMEI assignment for all products under this category.'
    )