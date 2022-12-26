from odoo import api,fields,models
class Contacts(models.Model):
	_inherit = 'res.partner'

	is_vendor = fields.Boolean(string = "Is Vendor")
	is_sale = fields.Boolean(string = "Is Sale")