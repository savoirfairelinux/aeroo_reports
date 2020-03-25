# © 2008-2014 Alistek
# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# © 2016-2020 Savoir-faire Linux
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

{
    'name': 'Aeroo Reports',
    'version': '2.2.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': 'Enterprise grade reporting solution',
    'author': 'Alistek',
    'maintainer': 'Savoir-faire Linux',
    'website': 'https://savoirfairelinux.com',
    'depends': ['mail'],
    'external_dependencies': {
        'python': ['aeroolib', 'babel', 'genshi'],
    },
    'data': [
        "security/security.xml",
        "views/mail_template.xml",
        "views/report_aeroo_assets.xml",
        "data/ir_config_parameter.xml",
        "data/report_aeroo_data.xml",
        "views/ir_actions_report.xml",
        "security/ir.model.access.csv",
    ],
    'demo': ["demo/report_sample.xml"],
    "license": "GPL-3 or any later version",
    'installable': True,
}
