from odoo import models, fields


class SaleOrder(models.Model):
  _inherit = 'sale.order'

  active = fields.Boolean(default=True)

  def unlink(self):
    for record in self:
      if record.active:
        record.active = False
      else:
        super().unlink()
