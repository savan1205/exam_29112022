from odoo import api,fields,models

class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'


   no_update = fields.Boolean(related="company_id.no_update",config_parameter="exam_29112022.no_update",string="No Update",readonly=False)

class Company(models.Model):
   _inherit="res.company"

   no_update = fields.Boolean(string="No Update")



