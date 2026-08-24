{
    "name": "Mobile IMEI Settings at Manufacturer level",
    "summary": "Add IMEI tracking and settings for mobile devices in repairs",
    "version": "18.0.1.0.0",
    "category": "Manufacturing/Repair",
    'author': 'Coder4web, Odoo Community Association (OCA)',
    "website": "https://github.com/OCA/repair",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "depends": [
        "repair_manufacturer",
        "repair_imei",
    ],
    "data": [
        "views/res_partner_view.xml"
    ],
    "auto_install": True,
    "installable": True,
    "application": False,
}