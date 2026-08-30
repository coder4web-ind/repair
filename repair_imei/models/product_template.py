from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    imei_required = fields.Selection(
        [("yes", "Yes"), ("no", "No"), ("parent", "Parent")],
        string="IMEI Required",
        compute="_compute_imei_required",
        store=True,
        readonly=False,
        help="Inherits requirement setting from category, but can be manually toggled.",
    )

    @api.depends("categ_id.imei_required")
    def _compute_imei_required(self):
        for template in self:
            if template.categ_id:
                template.imei_required = template.categ_id.imei_required
