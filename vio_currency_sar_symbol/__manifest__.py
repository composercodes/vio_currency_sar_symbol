{
    "name": "Saudi Riyal New Currency Symbol",
    "version": "16.0.1.0.0",
    "description": "Saudi Riyal (SAR) Currency New Symbol",
    "summary": "SAR New Symbol",
    "author": "ComposerCodes",
    "website": "https://www.linkedin.com/in/composercodes/",
    "category": "Tools",
    "depends": ["base", "web"],
    "data": [
        "data/res_currency_data.xml",
    ],
    "assets": {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss',
             'vio_currency_sar_symbol/static/src/scss/style.scss'),
        ], 'web.report_assets_pdf': [
            ('append', 'vio_currency_sar_symbol/static/src/scss/report.scss'),
        ], 'point_of_sale.assets': [
            ('append', 'vio_currency_sar_symbol/static/src/scss/pos.scss'),
        ], 'account_reports.assets_financial_report': [
            'vio_currency_sar_symbol/static/src/scss/account_financial_report.scss',
        ], 'web.assets_backend': [
            'vio_currency_sar_symbol/static/src/scss/account_financial_report.scss',
        ], 'web.report_assets_common': [
            'vio_currency_sar_symbol/static/src/scss/report.scss',
        ],
    },
    "images": ["static/description/banner.jpeg"],
    "license": "OPL-1",
    "auto_install": False,
    "application": False,
}
