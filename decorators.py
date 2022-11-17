from functools import wraps
from flask import g,url_for,redirect
def login_requried(func):
    #保留func的信息
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('user.login'))
    return inner


