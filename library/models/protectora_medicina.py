# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProtectoraMedicina(models.Model):
    _name = 'protectora.medicina'

    imatge = fields.Binary()
    nom = fields.Char(string="Nom")
    marca = fields.Char(string="Marca")
    unitats = fields.Float("Quantitat en unitats")
    preu = fields.Float("Preu")
