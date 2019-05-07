# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class ProtectoraInventari(models.Model):
    _name = 'protectora.inventari'

    imatge = fields.Binary()
    data = fields.Date(string="Data")
    llistamenjar = fields.Many2Many('protectora.menjar', string="Llista de menjar")

    @api.onchange('data')
    def onchange_date(self):
        today = fields.Date.today()
        if self.data and self.data > today:
            raise exceptions.UserError(
                "La data d'entrada hauria de ser anterior a avui."
            )
