from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"
    imei_required = fields.Boolean(
        string="IMEI Required",
        help='Enforce IMEI assignment for all products under this manufacturer.'
    )
