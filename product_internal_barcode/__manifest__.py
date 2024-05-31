{
    'name': 'Product internal barcode',
    'version': '16.0.0.0.0',
    'summary': 'Product internal barcode',
    'installable': True,
    'auto_install': False,
    'application': False,
    'depends': [
        'product',
        'point_of_sale',
    ],
    'data': [
        'views/product_template.xml',
        'views/product_product.xml',
    ],
    'assets': {
        'point_of_sale.assets': ['product_internal_barcode/static/src/js/**/*']
    }

        
}
