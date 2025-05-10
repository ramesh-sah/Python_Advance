from odoo import http

class CustomController(http.Controller):
    @http.route('/custom/route', auth='public')
    def custom_handler(self):
        return "Hello from Custom Module!"