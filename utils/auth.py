from functools import wraps
from flask import redirect, session, url_for

def with_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))  # Redirect to login page if not logged in
        return f(*args, **kwargs)  # Continue to the original function if logged in
    return decorated_function

