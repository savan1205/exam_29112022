from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit="sale.order.line"

    surplus_charge = fields.Float(readonly=True, string="surplus_charge: ")
   
	

	
		