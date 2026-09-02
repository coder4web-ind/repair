# Copyright 2026 Mukesh Mishra, Coder4web
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestRepairManufacturer(TransactionCase):
    """Test suite for repair manufacturer settings and restrictions."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.manufacturer_partner = cls.env["res.partner"].create(
            {
                "name": "Apple Manufacturer",
                "is_manufacturer": True,
            }
        )
        cls.customer_partner = cls.env["res.partner"].create(
            {
                "name": "John Customer",
                "is_manufacturer": False,
            }
        )
        cls.repair_order = cls.env["repair.order"].create(
            {
                "partner_id": cls.customer_partner.id,
                "manufacturer_id": cls.manufacturer_partner.id,
            }
        )

    def test_01_partner_is_manufacturer(self):
        """Test that the manufacturer flag is correctly set."""
        self.assertTrue(self.manufacturer_partner.is_manufacturer)
        self.assertFalse(self.customer_partner.is_manufacturer)

    def test_02_repair_order_manufacturer_assignment(self):
        """Test that a repair order can link a manufacturer correctly."""
        self.assertEqual(
            self.repair_order.manufacturer_id, self.manufacturer_partner
        )
        self.assertEqual(self.repair_order.partner_id, self.customer_partner)