{
    "name" : "Khmer Reports",
    "summary": """
            This addon will add 4 new print options on Purchase and Inventory APP
        """,
    "version": "19.0.1.0.0",
    "author": "Raksmey",
    "license": "AGPL-3",
    "website": "",
    "category": "Purchase/Localizations and Inventory/Localizations",
    "depends": ["purchase", "stock", "purchase_request", "report_layout_template", "project"],
    "data": [
        "report/report_paperformat.xml",
        "views/purchase_order_views.xml",
        "views/project_project_views.xml",
        'report/report_purchase_request.xml',
        'report/report_purchase_order.xml',
        'report/report_stock_receipt.xml',
        'report/report_stock_delivery.xml',
    ],
    "installable": True,
    "application": False,
}