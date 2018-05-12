import unittest
from unittest.mock import patch, MagicMock, call

from webfaction.webflib import WebFactionDBUser, WebFactionXmlRpc, API_URL
from xmlrpc import client as xmlrpclib
from http import client as httplib


class WebflibTest(unittest.TestCase):
    def test_should_store_creadentials_in_dedicated_object(self):
        username = "username"
        password = "password"
        db_type = "mysql"

        unit = WebFactionDBUser(username, password, db_type)

        self.assertEqual(username, unit.username)
        self.assertEqual(password, unit.password)
        self.assertEqual(db_type, unit.db_type)

    @patch('xmlrpc.client.Server')
    def test_should_init_WebFactionXmlRpc_object_with_defined_user_and_pass_and_call_login(self, mock_xmlrpc):
        username = "usr1"
        password = "pwd1"
        server_login_mock = MagicMock()
        server_login_mock.login.return_value = (None, username)
        mock_xmlrpc.return_value = server_login_mock

        unit = WebFactionXmlRpc(user=username, password=password)
        mock_xmlrpc.assert_called_with(API_URL, transport=None)
        self.assertEqual(unit.account, username)

    @patch('xmlrpc.client.Server')
    def test_should_call_list_app(self, mock_xmlrpc):
        username = "usr1"
        password = "pwd1"
        server_login_mock = MagicMock()
        server_login_mock.login.return_value = (None, username)
        mock_xmlrpc.return_value = server_login_mock
        mock_xmlrpc.list_app.return_value = None

        expected_calls = [
            call('https://api.webfaction.com/', transport=None),
            call().login('usr1', 'pwd1'),
            call().list_apps(None)
        ]
        unit = WebFactionXmlRpc(user=username, password=password)
        unit.list_apps()
        mock_xmlrpc.assert_has_calls(expected_calls, any_order=False)
