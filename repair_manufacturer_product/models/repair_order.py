from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class RepairOrder(models.Model):
    _inherit = "repair.order"

    category_id = fields.Many2one(
        comodel_name="product.category",
        string="Product Category",
        help="Filter products by category for the selected manufacturer.",
    )
    allowed_category_ids = fields.Many2many(
        comodel_name="product.category",
        compute="_compute_allowed_category_ids",
        string="Allowed Categories",
        store=False
    )

    @api.depends("manufacturer_id")
    def _compute_allowed_category_ids(self):
        for repair in self:
            if not repair.manufacturer_id:
                repair.allowed_category_ids = False
                continue
            
            products = self.env["product.product"].search(
                [("manufacturer_id", "=", repair.manufacturer_id.id)]
            )
            repair.allowed_category_ids = products.mapped("categ_id")

    @api.onchange("manufacturer_id")
    def _onchange_manufacturer_id(self):
        """Reset downstream selections when manufacturer changes."""
        self.category_id = False
        self.product_id = False

    @api.onchange("category_id")
    def _onchange_category_id(self):
        """Reset product selection when category changes."""
        self.product_id = False