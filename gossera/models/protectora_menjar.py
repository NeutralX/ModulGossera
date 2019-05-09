# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProtectoraMenjar(models.Model):
    _name = 'protectora.menjar'

    imatge = fields.Binary()
    nom = fields.Char(string="Nom")
    marca = fields.Char(string="Marca")
    quantitat = fields.Float("Quantitat en kg")
    preu = fields.Float("Preu")
