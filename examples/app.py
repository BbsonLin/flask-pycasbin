from flask import Flask
from flask_pycasbin import PyCasbin

casbin = PyCasbin()

app = Flask(__name__)

casbin.init_app(app)
print(casbin.enforcer)

print(casbin.enforcer.get_policy())
