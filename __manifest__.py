# -*- coding: utf-8 -*-
# © 2008-2014 Alistek
# © 2016 Savoir-faire Linux
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

{
    'name': 'Aeroo Reports',
    'version': '10.0.1.0.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': 'Enterprise grade reporting solution',
    'author': 'Alistek',
    'website': 'http://www.alistek.com',
    'complexity': "easy",
    'depends': ['base'],
    'external_dependencies': {
        'python': ['aeroolib', 'genshi', 'simplejson'],
    },
    'data': [
        "security/security.xml",
        "report_view.xml",
        "data/ir_config_parameter.xml",
        "data/report_aeroo_data.xml",
        "security/ir.model.access.csv",
    ],
    'demo': ["demo/report_sample.xml"],
    "license": "GPL-3 or any later version",
    'installable': True,
    'active': False,
    'application': True,
    'auto_install': False,
}
