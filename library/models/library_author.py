# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char(string="Name")
    date = fields.Date(string="Birth Date")
    place = fields.Char(string="Place of birth")
    writer = fields.Boolean("Is active")

    @api.onchange('date')
    def onchange_date(self):
        today = fields.Date.today()
        if self.date and self.date > today:
            raise exceptions.UserError(
                "La data hauria de ser anterior a avui."
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