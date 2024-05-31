from odoo import models, fields


class ProductCategory(models.Model):
  _inherit = 'product.category'
  active = fields.Boolean(default=True)

  def unlink(self):
    for record in self:
      if record.active:
        record.active = False
      else:
        super().unlink()
