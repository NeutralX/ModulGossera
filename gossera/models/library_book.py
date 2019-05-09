# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string="Name")
    copies = fields.Boolean("Have copies")
    image = fields.Binary()
    pages = fields.Integer(string="# Pages")
    isbn = fields.Char(string="ISBN", size=13)
    date = fields.Date(string="Release Date")
    category_id = fields.Many2one("library.category", string="Category")
    author = fields.Many2one("library.author", string="Author")

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