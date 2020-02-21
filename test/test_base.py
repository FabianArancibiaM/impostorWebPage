from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class mainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprint())
