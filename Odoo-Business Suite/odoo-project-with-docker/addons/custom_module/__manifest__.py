{
    'name': 'Custom Module',
    'version': '1.0',
    'summary': 'Custom Odoo Module',
    'sequence': 10,
    'description': """
    Custom Odoo Module with Docker Setup
    """,
    'category': 'Customization',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}