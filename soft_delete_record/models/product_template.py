from odoo import models


class ProductTemplate(models.Model):
  _inherit = 'product.template'

  def unlink(self):
    for record in self:
      if record.active:
        record.active = False
      else:
        super().unlink()
