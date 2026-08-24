{
    "name": "Repair Manufacturer Product Glue",
    "summary": "Enable Manufacturer and product relation for electronic devices",
    "version": "18.0.1.0.0",
    "category": "Manufacturing/Repair",
    "author": "Coder4web, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/repair",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "depends": [
        "repair_manufacturer",
        "product_manufacturer",
    ],
    "data": [
        "views/repair_order_views.xml",
    ],
    "auto_install": True,
    "installable": True,
}