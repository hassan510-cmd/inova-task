from odoo import models

class ResPartner(models.Model):
  _inherit = 'res.partner'

  def unlink(self):
    for record in self:
      if record.active:
        record.active = False
      else:
        super().unlink()
