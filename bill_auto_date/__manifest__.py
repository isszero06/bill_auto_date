# -*- coding: utf-8 -*-
{
    'name': 'Bill Date today Date',
    'version': '5.0.1',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,

    'summary': """If Sales order Date less than today date and when confirm order the order date not change""",

    'description': """
        The standard situation of the Odoo system, when confirming the Bill,
        the Bill Date field is empty and must be filled in manually,
        but with this modification, the date field will be equal to today's date automatically ” ,


        """,
    'depends': [
        'account',
    ],
    'data': [
    ],
    'license': 'OPL-1',
    # 'live_test_url': 'https://www.youtube.com/watch?v=T82sTeIwrm8',
    'images': ['static/description/bill_date_today.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 0.00,
    'currency': 'EUR',
    "pre_init_hook": "pre_init_check",
}
