{
    'name': 'JS PoS Odoo',

    'version': '14.0.0.0',

    'author': "Luis Felipe Paternina",

    'contributors': ['Luis Felipe Paternina'],

    'website': "",

    'category': 'PoS',

    'depends': [

        'base',
        'base_automation',
        'point_of_sale',
        'sale_management',

    ],

    'data': [

        'views/assets.xml',
              
    ],

    'qweb': [
        'static/src/xml/view.xml',
        'static/src/xml/payment.xml',
    ],

    'installable': True
}
