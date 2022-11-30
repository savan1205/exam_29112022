from odoo import api, fields, models
from datetime import date, datetime


class SurplusChargeRules(models.Model):
	_name = 'surplus.charges.configuration'
	_description = 'Configure Surplus Charges'
	_rec_name = "product_id"

	product_id = fields.Many2one(comodel_name="product.product",
	                             string="Product", domain="[('is_surplus_charges','=',True),('detailed_type','=','service')]")

	surplus_charges = fields.Float(string="Surplus Charges%")
	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	is_active = fields.Boolean(string="Active")
	display_name = fields.Char(string="Display Name")

	# this function archives the record if  the end date has been reached
	@api.model
	def check_end_date(self):
	    if self.end_date.day == Date.today().day and self.end_date.month == Date.today().month:
	        self.active = False
	

	# In this function the display name is shown by using name_get 
	# to combine the product_id and surplus_charges 
	# @api.onchange('product_id', 'surplus_charges')
	# def name_get(self):
	#     result = []
	#     for rec in self:
	#         result.append(("%s - %s" % (rec.product_id.name, rec.surplus_charges)))
	#     self.display_name = result
	#     return result





	
	
