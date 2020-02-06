import os

from flask import Flask, session, redirect
from flask_pycasbin import PyCasbin

from decorators import permission_required

casbin = PyCasbin()

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY')
)

casbin.init_app(app)
print(casbin.enforcer)

print(casbin.enforcer.get_policy())


@permission_required()
@app.route('/')
def index():
    return 'Index Page'


@app.route('/login')
def login():
    session['user'] = 'admin'
    return redirect('/admin')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/admin')
@permission_required()
def admin():
    return 'Admin Page'


@app.route('/admin/info')
@permission_required()
def admin_info():
    return 'Admin Info'
