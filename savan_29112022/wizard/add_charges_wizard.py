from odoo import api, fields, models


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
                                  string="Product",domain="[('is_active','=',True)]")
    surplus_charges = fields.Float(related="product_id.surplus_charges",string="Surplus Charges%")
    start_date = fields.Date(related="product_id.start_date",string="Start Date")

    def btn_add(self):
        add_data = []
        for result in self.product_id:
            add_data.append((0,0,{
                'product_id':result.product_id.id,
                'price_unit':result.surplus_charges,
                }))    

        self.sale_order_id.write({
            'order_line':add_data,
            })
