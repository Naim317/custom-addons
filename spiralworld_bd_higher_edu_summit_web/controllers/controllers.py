import sys

from addons.website.controllers.main import QueryURL
from odoo import http
from odoo.http import request,Response
from json import dumps
from base64 import b64encode
from odoo.tools import date_utils, datetime, timedelta, date
from PIL import ImageColor
import base64

class SpiralworldHigherEduSummitWeb(http.Controller):

    @http.route(['/home'], website=True, csrf=False, type='http', auth="public")
    def sprialworld_higher_edu_home(self, **kw):
        summit = request.env['spiral.world.higher.edu.summit'].sudo().search([('id','=',1)])
        puser = request.env.user

        values = {}
        values.update({
            'menu_action': "home",
            'puser': puser,
            'users': True,
            'about': True,
            'chief_guest': True,
            # 'home_menu': True,
            'slider': True,
            'sponsor': True,
            'suvenior': True,
            'summit': summit,
        })
        return request.render("spiralworld_bd_higher_edu_summit_web.spiralworld_edu_master",values)

    @http.route(['/participating-institute'], website=True, csrf=False, type='http', auth="public")
    def sprialworld_higher_edu_participating_institute(self, **kw):
        expo_zones = request.env['spiral.world.higher.expo.zone'].sudo().search([('edu_summit_id', '=', 1)])
        puser = request.env.user

        values = {}
        values.update({
            'menu_action': "participating_institute",
            'puser': puser,
            'users': True,
            'participating_institute': True,
            'expo_zones': expo_zones,
        })
        return request.render("spiralworld_bd_higher_edu_summit_web.spiralworld_edu_master", values)

    @http.route(['/participating-institute/<int:expo_zone_id>'], website=True, csrf=False, type='http', auth="public")
    def sprialworld_higher_edu_participating_institute_id(self, expo_zone_id = False, **kw):
        expo_zone_details = request.env['spiral.world.higher.expo.zone'].sudo().search([('id', '=', expo_zone_id)])
        puser = request.env.user

        values = {}
        values.update({
            'menu_action': "participating_details",
            'puser': puser,
            'users': True,
            'participating_details': True,
            'expo_zone_details': expo_zone_details,
        })
        return request.render("spiralworld_bd_higher_edu_summit_web.spiralworld_edu_master", values)

    @http.route(['/my-meeting/<int:meeting_id>'], website=True, csrf=False, type='http', auth="public")
    def sprialworld_summit_higher_edu_meeting(self, meeting_id=False, **kw):
        puser = request.env.user
        meetings = request.env['spiral.world.higher.meeting'].sudo().search([('id', '=', meeting_id)])
        videocall_server_url = request.env['ir.config_parameter'].sudo().get_param(
            'acs_jitsi_meet.video_call_server_url')
        meeting_user = ""
        if meetings:
            for value in meetings.counselor_ids:
                if value.id == puser.id and meetings.state == 'draft':
                    meeting_user = "done"
        values = {}
        values.update({
            'menu_action': "my_meeting",
            'puser': puser,
            'users': False,
            'my_meeting': True,
            'sponsor': True,
            'meetings': meetings,
            'meeting_user': meeting_user,
            'server_name': videocall_server_url.split("//")[1],
            'site_url': 'http://127.0.0.1:8069',
        })
        return request.render("spiralworld_bd_higher_edu_summit_web.spiralworld_edu_master", values)

    @http.route(['/chat'], type='http', auth="user", website=True, csrf=False, methods=['POST'])
    def sprialworld_higher_edu_chat(self, **kw):
        puser = request.env.user
        print("test value")
        print(puser.id)
        request.env['spiral.world.higher.expo.chat'].sudo().create({
            'send_by': puser.id,
            'message': kw['message'],
            'edu_expo_zone_id': kw['edu_expo_zone_id'],
        })
        return "Success"

    @http.route(['/get/chat/<int:edu_expo_zone_id>'], type='http', auth="user", website=True, csrf=False, methods=['GET'])
    def spiralworld_agm_qa_list(self, edu_expo_zone_id=False, **kw):
        puser = request.env.user
        # chat = request.env['spiral.world.agm.chat'].sudo().search(['&','|','&',('agm_id', '=', agm_id),('send_by', '=', puser.id),('receive_by', '=', puser.id),('state', 'in', ['draft', 'accept'])])
        result = []
        chat = request.env['spiral.world.higher.expo.chat'].sudo().search([('edu_expo_zone_id', '=', edu_expo_zone_id)])
        if chat:
            for line in chat:
                data = {
                    "id": line.id,
                    "message": line.message,
                    "send_by": line.send_by.id,
                    "send_name": line.send_by.name,
                    "receive_by": line.receive_by.id,
                    "receive_name": line.receive_by.name,
                    "create_date": line.create_date,
                }
                result.append(data)

        json_event_data = dumps(result, default=date_utils.json_default)
        return Response(json_event_data, headers={'content-type': 'application/json'}, status=200)

    @http.route(['/login'], website=True, csrf=False, type='http', auth="public")
    def sprialworld_higher_summit_login(self, **kw):
        puser = request.env.user
        values = {}
        values.update({
            'menu_action': "login",
            'puser': puser,
            'users': False,
            'login': True,
            'sponsor': True,
        })
        return request.render("spiralworld_bd_higher_edu_summit_web.spiralworld_edu_master", values)

    @http.route(['/login/check'], website=True, csrf=False, type='http', auth="public")
    def autologin(self, **kw):
        puser = request.env.user
        dbname = "vafdb"
        login = request.httprequest.form['email']
        password = request.httprequest.form['password']
        try:
            uid = request.session.authenticate(dbname, login, password)
            request.params['login_success'] = True
            return http.redirect_with_hash('/participating-institute')
        except Exception as e:
            return http.redirect_with_hash('/login')