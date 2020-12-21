# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class AccountTax(orm.Model):
    _inherit = 'account.tax'
    _columns = {
        'non_taxable_nature': fields.selection([
            ('N1', 'Escluse ex art. 15'),
            ('N2', 'Non soggette'),
            ('N3', 'Non imponibili'),
            ('N4', 'Esenti'),
            ('N5', 'Regime del margine / IVA non esposta in fattura'),
            ('N6', 'Inversione contabile'),
            ('N7', 'IVA assolta in altro stato UE'),
            ('N2.1', 'non soggette ad IVA ai sensi degli artt. da 7 a 7-septies del DPR 633/72'),
            ('N2.2', 'non soggette – altri casi'),
            ('N3.1', 'non imponibili – esportazioni'),
            ('N3.2', 'non imponibili – cessioni intracomunitarie'),
            ('N3.3', 'non imponibili – cessioni verso San Marino'),
            ('N3.4', 'non imponibili – operazioni assimilate alle cessioni all’esportazione'),
            ('N3.5', 'non imponibili – a seguito di dichiarazioni d’intento'),
            ('N3.6', 'non imponibili – altre operazioni che non concorrono alla formazione del plafond'),
            ('N6.1', 'inversione contabile – cessione di rottami e altri materiali di recupero'),
            ('N6.2', 'inversione contabile – cessione di oro e argento puro'),
            ('N6.3', 'inversione contabile – subappalto nel settore edile'),
            ('N6.4', 'inversione contabile – cessione di fabbricati'),
            ('N6.5', 'inversione contabile – cessione di telefoni cellulari'),
            ('N6.6', 'inversione contabile – cessione di prodotti elettronici'),
            ('N6.7', 'inversione contabile – prestazioni comparto edile e settori connessi'),
            ('N6.8', 'inversione contabile – operazioni settore energetico'),
            ('N6.9', 'inversione contabile – altri casi'),
            ], string="Non taxable nature"),
        'payability': fields.selection([
            ('I', 'Immediate payability'),
            ('D', 'Deferred payability'),
            ('S', 'Split payment'),
            ], string="VAT payability"),
        'law_reference': fields.char(
            'Law reference', size=128),
    }

    def get_tax_by_invoice_tax(self, cr, uid, invoice_tax, context=None):
        if ' - ' in invoice_tax:
            tax_descr = invoice_tax.split(' - ')[0]
            tax_ids = self.search(cr, uid, [
                ('description', '=', tax_descr),
                ], context=context)
            if not tax_ids:
                raise orm.except_orm(
                    _('Error'), _('No tax %s found') %
                    tax_descr)
            if len(tax_ids) > 1:
                raise orm.except_orm(
                    _('Error'), _('Too many tax %s found') %
                    tax_descr)
        else:
            tax_name = invoice_tax
            tax_ids = self.search(cr, uid, [
                ('name', '=', tax_name),
                ], context=context)
            if not tax_ids:
                raise orm.except_orm(
                    _('Error'), _('No tax %s found') %
                    tax_name)
            if len(tax_ids) > 1:
                raise orm.except_orm(
                    _('Error'), _('Too many tax %s found') %
                    tax_name)
        return tax_ids[0]





"""
('N1'   ,'Escluse ex art. 15'),
('N2'   ,'Non soggette'),
('N3'   ,'Non imponibili'),
('N4'   ,'Esenti'),
('N5'   ,'Regime del margine / IVA non esposta in fattura'),
('N6'   ,'Inversione contabile'),
('N7'   ,'IVA assolta in altro stato UE'),
('N2.1','non soggette ad IVA ai sensi degli artt. da 7 a 7-septies del DPR 633/72'),
('N2.2','non soggette – altri casi'),
('N3.1','non imponibili – esportazioni'),
('N3.2','non imponibili – cessioni intracomunitarie'),
('N3.3','non imponibili – cessioni verso San Marino'),
('N3.4','non imponibili – operazioni assimilate alle cessioni all’esportazione'),
('N3.5','non imponibili – a seguito di dichiarazioni d’intento'),
('N3.6','non imponibili – altre operazioni che non concorrono alla formazione del plafond'),
('N6.1','inversione contabile – cessione di rottami e altri materiali di recupero'),
('N6.2','inversione contabile – cessione di oro e argento puro'),
('N6.3','inversione contabile – subappalto nel settore edile'),
('N6.4','inversione contabile – cessione di fabbricati'),
('N6.5','inversione contabile – cessione di telefoni cellulari'),
('N6.6','inversione contabile – cessione di prodotti elettronici'),
('N6.7','inversione contabile – prestazioni comparto edile e settori connessi'),
('N6.8','inversione contabile – operazioni settore energetico'),
('N6.9','inversione contabile – altri casi'),


"""