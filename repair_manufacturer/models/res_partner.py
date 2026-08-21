from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"
    is_manufacturer = fields.Boolean(
        string="Is Manufacturer",
        default=False,
        help="Check if this partner is an OEM or device manufacturer.",
    )