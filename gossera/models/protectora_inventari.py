# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProtectoraInventari(models.Model):
    _name = 'protectora.inventari'

    imatge = fields.Binary()
    data = fields.Date(string="Data")
    llistamenjar = fields.Many2many('protectora.menjar', string="Llista de menjar")


    @api.onchange('data')
    def onchange_date(self):
        today = fields.Date.today()
        if self.data and self.data > today:
            raise exceptions.UserError(
                "La data d'entrada hauria de ser anterior a avui."
            )

# class library(models.Model):
#     _name = 'library.library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100