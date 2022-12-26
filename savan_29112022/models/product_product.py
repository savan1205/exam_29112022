from odoo import api,fields,models
class ProductTemplate(models.Model):
	_inherit = 'product.template'

	is_surplus_charges = fields.Boolean(string = "Is Surplus Charges")
	show_product = fields.Boolean(string = "Show Product in SO")
	no_update = fields.Boolean(compute = "_get_update_value", string = "No Update")

	def _get_update_value(self):
		self.no_update = self.env['ir.config_parameter'].sudo().get_param('exam_29112022.no_update')
		return self.no_update