from odoo import api, fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    imei_required = fields.Boolean(
        compute="_compute_imei_required",
        store=True,
        string="IMEI Required",
    )

    @api.depends(
        "product_id",
        "product_id.imei_required",
        "product_id.categ_id",
        "product_id.categ_id.imei_required",
        "manufacturer_id",
        "manufacturer_id.imei_required",
    )
    def _compute_imei_required(self):
        for record in self:
            imei_settings = "parent"

            # 1. Check Product level
            if record.product_id and hasattr(record.product_id, "imei_required"):
                imei_settings = record.product_id.imei_required or "parent"

            # 2. Fall back to Category level if set to "parent"
            if (
                imei_settings == "parent"
                and record.product_id
                and record.product_id.categ_id
                and hasattr(record.product_id.categ_id, "imei_required")
            ):
                imei_settings = record.product_id.categ_id.imei_required or "parent"

            # 3. Fall back to Manufacturer level if Category is still "parent"
            if (
                imei_settings == "parent"
                and record.manufacturer_id
                and hasattr(record.manufacturer_id, "imei_required")
            ):
                imei_settings = record.manufacturer_id.imei_required or "no"

            record.imei_required = imei_settings == "yes"
