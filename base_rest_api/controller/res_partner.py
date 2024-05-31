import json
from odoo import http
from odoo.http import request, Response


class ContactController(http.Controller):

  @http.route(
      ['/api/contact/<int:id>'],
      type='http',
      auth='user',
      methods=['GET'],
      csrf=False,
  )
  def get_contact(self, id):
    contact = request.env['res.partner'].sudo().browse(id)
    if not contact.exists():
      return Response(status=404)
    return json.dumps({
        'id': contact.id,
        'name': contact.name,
        'email': contact.email,
        'phone': contact.phone,
    })

  @http.route(
      '/api/contact',
      type='json',
      auth='user',
      methods=['POST'],
      csrf=False,
  )
  def create_contact(self, **kwargs):
    data = request.get_json_data()
    try:
      contact = request.env['res.partner'].sudo().create(data)
      return {'id': contact.id, 'message': 'Contact created successfully'}
    except Exception as e:
      return Response(str(e), status=400)

  @http.route(
      ['/api/contact/<int:id>'],
      type='json',
      auth='user',
      methods=['PUT'],
      csrf=False,
  )
  def update_contact(self, id, **kwargs):
    contact = request.env['res.partner'].sudo().browse(id)
    data = request.get_json_data()
    if not contact.exists():
      return Response(status=404)
    try:
      contact.write(data)
      return {'id': contact.id, 'message': 'Contact updated successfully'}
    except Exception as e:
      return Response(str(e), status=400)
