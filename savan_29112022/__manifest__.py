{
    'name': 'Surplus Charges',
    'version': '15.0.1.1',
    'summary': 'Apply Surplus Charges',
    'sequence': 9,
    'description': """
        This module contains all the features of Configuring Sales Orders to add Surplus Charges to them.
    """,
    'depends': ['sale_management'],
    'data': [
        'security/surplus_charges_security.xml',
        'security/ir.model.access.csv',

        'report/sale_report_inherit.xml',

        'data/archive_record.xml',
        'wizard/add_charges_wizard_views.xml',

        'views/product_product_views.xml',
        'views/surplus_charges_rules_views.xml',
        'views/sale_order_inherit_views.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,


    'license': 'LGPL-3',

}
