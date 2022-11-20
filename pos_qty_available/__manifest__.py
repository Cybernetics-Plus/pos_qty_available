# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#
#    Copyright (C) 2021-TODAY Cybernetics Plus Technologies (<https://www.cybernetics.plus>).
#    Author: Cybernetics Plus Techno Solutions (<https://www.cybernetics.plus>)
#
#    POS Extension Module for Odoo
#
#    Show Available Product Only
#    This is a simple solution to reduce POS resources and less time
#    to start devices with a large amount of product list.
#
###################################################################################

{
    "name": "POS Qty Available",
    "version": "13.0.1.0.6",
    "summary": """ 
            Show Available Product Only
            .""",
    "description": """ 
            Show Available Product Only
            This is a simple solution to reduce POS resources and less time to start devices with a large amount of product list.
            .""",
    "author": "Cybernetics Plus",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus/module/pos-show-available-product-only",
    "images": ["static/description/banner.gif"],
    "category": "Point Of Sale",
    "data": [
        "views/inherited_pos_config_form_view.xml",
    ],
    "depends": ["point_of_sale"],
    "license": "OPL-1",
    "price": 29.99,
    "currency": "EUR",
    "installable": True,
    "application": True,
    "auto_install": False,
    "contributors": [
        "Developer <dev@cybernetics.plus>",
    ],
    "assets": {
        "point_of_sale.assets": [
             "pos_qty_available/static/src/js/pos_qty_available.js",
        ],
    },
}