from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class SurplusChargeRulesConfiguration(models.Model):
    _name = 'surplus.charges.configuration'
    _description = 'Configure Surplus Charges'
    _rec_name = "product_id"

    product_id = fields.Many2one(comodel_name="product.product",
                                 string="Product", domain="[('is_surplus_charges','=',True),('detailed_type','=','service')]")
    surplus_charges = fields.Float(string="Surplus Charges%")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    active = fields.Boolean(string="Active",default=True)
    display_name = fields.Char(string="Display Name", compute="compute_generate_display_name", readonly=True)

    _sql_constraints = [
        ('product_id', 'unique (product_id)', 'The product already Exists in a record, Please Select a Unique Product !'),
    ]
    # this function archives the record if the end date has been reached
    def cron_check_charge_validity(self):
        charges_record = self.env["surplus.charges.configuration"].search([]).filtered(lambda x:x.end_date <= date.today())
        print("==========================",charges_record)
        for rec in charges_record:
            rec.active = False

    # Validate SurplusCharge
    @api.onchange('surplus_charges')
    def check_charge_percentage(self):
        if 0 <= self.surplus_charges <= 100:
            pass
        else:
            raise ValidationError("Charges can only be in between 0 and 100")

    @api.onchange('start_date')
    def check_date(self):
        for rec in self:
            if rec.start_date:
                if rec.start_date >= date.today():
                    pass
                else:
                    raise ValidationError("You cannot enter date previous from today's date")

    # In this function the display name is shown by using name_get
    # to combine the product_id and surplus_charges
    @api.depends('product_id','surplus_charges')
    def compute_generate_display_name(self):
        for record in self:
            if not record.product_id:
                record.display_name = 'New'
            else:
                record.display_name = (
                    str(record.product_id.name) + "- (" + str(record.surplus_charges) + "%)"
                )

