from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError
class SurplusChargesWizard(models.TransientModel):
    _name = 'surplus.charges.wizard'
    _description = 'Fill surplus charges records into wizard'

    # This function is to get the current sale orders ID
    @api.model
    def _get_default_order(self):
        ctx = self._context
        if ctx.get('active_model') == 'sale.order':
            current_id = self.env['sale.order'].browse(ctx.get('active_ids')[0])
            print("----------------------",current_id)
            return current_id

    sale_order_id = fields.Many2one(readonly=True, comodel_name="sale.order", string="Order",default=_get_default_order)
    product_id = fields.Many2one("surplus.charges.configuration",
                                  string="Product",domain="[('active','=',True)]")
    surplus_charges = fields.Float(related="product_id.surplus_charges",string="Surplus Charges%")
    start_date = fields.Date(related="product_id.start_date",string="Start Date")

    def btn_add(self):
        ''' This Function validates cases for adding surplus charge
            Products in current Sales Order Record'''
        sub = 0
        for order_lines in self.sale_order_id.order_line:
            # print("order_lines----------",order_lines)
            if order_lines.product_id.is_surplus_charges == True and order_lines.product_id.detailed_type == 'service':
                order_lines.unlink()
            else:
                sub += order_lines.price_subtotal
                print("==============+++++=========",sub)

        for products in self.product_id:
            surplus_price_total = (sub * products.surplus_charges)/100
            print("-------------------------------------",surplus_price_total)
            add_data = []

            add_data.append((0,0,{
                'product_id':products.product_id.id,
                'price_unit':surplus_price_total,
            }))
            self.sale_order_id.write({
                'order_line':add_data,
                'extra_charges':surplus_price_total,
            })

