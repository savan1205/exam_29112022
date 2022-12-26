from odoo import fields, models

class SaleOrder(models.Model):
    _inherit="sale.order"

    extra_charges = fields.Float(readonly=True, string="Extra Charges")
    def get_surplus_charge(self):
        surplus_records_list = self.env['surplus.charges.configuration'].search([('active', '=', True)]).ids
        action_id = self.env.ref('savan_29112022.wizard_surplus_records_form').id

        ctx = {
            'surplus_records_list': surplus_records_list,
            'sale_id': self.id
        }

        return {
            "type": "ir.actions.act_window",
            "res_model": "surplus.charges.wizard",
            "view_type": "form",
            "view_mode": 'form',
            "view_id": action_id,
            "name": "Surplus Charge Wizard",
            'target': 'new',
            'context': ctx
        }
class SaleOrderLine(models.Model):
    _inherit="sale.order.line"

    is_surplus_charge = fields.Boolean(related="product_id.is_surplus_charges", string="surplus_charge: ")
   

