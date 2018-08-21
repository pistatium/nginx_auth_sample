# coding: utf-8

from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

SESSION_KEY = 'SESSION'


@app.route('/auth/login')
def login():
    response = make_response(redirect('/'))
    response.set_cookie(SESSION_KEY, '1')  # FIXME
    return response 


@app.route('/auth/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie(SESSION_KEY, '', expires=0)  # Delete cookie 
    return response 


@app.route('/auth/is_login')
def is_login():
    # FIXME
    if not request.cookies.get(SESSION_KEY):
        abort(401)
    return ''  # 200

