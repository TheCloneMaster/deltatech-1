# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "Website City",
    "category": "Website/Website",
    "summary": "City extension",
    "version": "15.0.1.0.1",
    "author": "Terrabit, Dorin Hongu",
    "license": "OPL-1",
    "website": "https://www.terrabit.ro",
    "depends": ["portal", "website_sale", "base_address_city"],
    "data": [
        "views/portal.xml",
        #     "views/assets.xml"
    ],
    "price": 5.00,
    "currency": "EUR",
    "images": ["static/description/main_screenshot.png"],
    "installable": True,
    "development_status": "Mature",
    "maintainers": ["dhongu"],
    "assets": {
        "web.assets_frontend": ["deltatech_website_city/static/src/js/portal.js"],
    },
}
