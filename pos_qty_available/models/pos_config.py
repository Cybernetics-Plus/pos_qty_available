# -*- coding: utf-8 -*-
from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    point_qty_available_id = fields.Boolean('Activate Module on this POS',default=True)
    point_qty_available_num = fields.Integer(string="Sequence", default=1)