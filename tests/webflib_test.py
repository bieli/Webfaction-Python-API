import unittest

from webfaction.webflib import WebFactionDBUser


class WebflibTest(unittest.TestCase):
    def test_should_store_creadentials_in_dedicated_object(self):
        username = "username"
        password = "password"
        db_type = "mysql"

        unit = WebFactionDBUser(username, password, db_type)

        self.assertEqual(username, unit.username)
        self.assertEqual(password, unit.password)
        self.assertEqual(db_type, unit.db_type)
