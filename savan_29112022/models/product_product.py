from odoo import api,fields,models

class ProductProduct(models.Model):
	_inherit = 'product.template'

	is_surplus_charges = fields.Boolean(string = "Is Surplus Charges")