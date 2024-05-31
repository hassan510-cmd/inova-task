from odoo import fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'
  

  internal_barcode = fields.Char(
    string='Internal Barcode',
    help='Internal Barcode',
  )