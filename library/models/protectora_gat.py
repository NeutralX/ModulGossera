# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProtectoraGos(models.Model):
    _name = 'protectora.gat'

    imatge = fields.Binary()
    nom = fields.Char(string="Nom")
    edat = fields.Integer(string="Edat")
    vacunat = fields.Boolean("Esta vacunat")
    sexe = fields.Char(string="Sexe")
    dataEntrada = fields.Date(string="Data Entrada")
    race = fields.Many2one("protectora.race.gat", string="Race")

    # isbn = fields.Char(string="ISBN", size=13)
    # date = fields.Date(string="Release Date")

    # author = fields.Many2one("library.author", string="Author")

    @api.onchange('dataEntrada')
    def onchange_date(self):
        today = fields.Date.today()
        if self.dataEntrada and self.dataEntrada > today:
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