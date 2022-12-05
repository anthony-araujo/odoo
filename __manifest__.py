# -*- coding: utf-8 -*-
###################################################################################
#
#    Retail IT & Solutions
#
#    Copyright (C) 2022-TODAY Retail IT & Solutions(<https://www.facebook.com/Retail-Solutions-Bolivia-100170668481500>).
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'Product Brand, Corner in Inventory',
    'version': '14.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Brand y Corner in Inventory',
    'author': 'Retail IT & Solutions',
    'company': 'Retail IT & Solutions',
    'maintainer': 'Retail IT & Solutions',
    'images': ['static/description/banner.png'],
    'website': 'https://www.facebook.com/Retail-Solutions-Bolivia-100170668481500',
    'depends': ['stock'],
    'data': [
        'views/brand_views.xml',
        'views/corner_views.xml',
        'views/rs_partner.xml',
        'views/rs_product.xml',

        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
