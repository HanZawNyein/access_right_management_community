from odoo import api, fields, models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        ids = super(IrUiMenu, self).search(args, offset=0, limit=None, order=order, count=False)
        # print("*" * 100)
        user = self.env.user
        user.clear_caches()
        # print(len(ids))
        hide_menu_ids = user.access_rights_management_ids.mapped('hide_menu_ids')
        # print(hide_menu_ids,"hide_menu_ids")
        ids = ids - hide_menu_ids
        # print(len(ids))
        # print("Hiding Menu.................")
        # print("*" * 100)
        return ids
