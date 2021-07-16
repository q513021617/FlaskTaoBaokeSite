import functools
from distutils import config
from flask import Flask, render_template, redirect, url_for, session, request,abort
from flask import request, jsonify
from itsdangerous import Serializer


def login_required():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                # 在请求头上拿到token
                token = session.get('username')
            except Exception as e:
                # 没接收的到token,给前端抛出错误
                return redirect("/admin/login")
            return func(*args, **kw)
        return wrapper
    return decorator