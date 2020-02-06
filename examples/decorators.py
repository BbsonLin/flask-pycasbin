from functools import wraps

from flask import request, session, abort
from flask_pycasbin.utils import check_permission


def permission_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if check_permission(request, session.get('user', None)):
                return fn(*args, **kwargs)
            else:
                abort(403, 'You have no permission to call this api')
        return wrapper
    return decorator
