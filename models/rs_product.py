# -*- coding: utf-8 -*-
from email.policy import default
import string
from odoo import fields, models
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    SkuPadre = fields.Char(u"Sku Padre", size=20, required=False, index=True, copy=False, default='')
    DescripcionCorta = fields.Char(u"Descripción Corta", size=200, required=False, index=True, copy=False, default='')
    Descripcion = fields.Char(u"Descripción", size=100, required=False, index=True, copy=False, default='')
    Etiqueta = fields.Char(u"Etiqueta", size=100, required=False, index=True, copy=False, default='')
