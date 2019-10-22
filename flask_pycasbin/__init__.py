import os

from casbin import Enforcer

basedir = os.path.abspath(os.path.dirname(__file__))


class PyCasbin(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['flask-pycasbin'] = self

        self._create_casbin_enforcer(app)

    def _create_casbin_enforcer(self, app):
        self.enforcer = Enforcer(model=f'{basedir}/rules/default_model.conf', adapter=f'{basedir}/rules/default_policy.csv')
