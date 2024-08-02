# -*- coding: utf-8 -*-

from odoo import models, api


class WebsiteSupportHook(models.AbstractModel):
    _name = 'website.support.hook'

    @api.model
    def _post_hook_v_2_0_3(self):
        module_self = self.env['ir.module.module'].search([('name', '=', 'website_support')])
        actions_todo = module_self and module_self.latest_version < '2.0.3'
        if actions_todo:
            sequence = self.env['ir.sequence'].search([('code', '=', 'website.support.ticket')])
            company = self.env['res.company'].search([], limit=1)
            if sequence and company:
                sequence.number_next = company.next_support_ticket_number
