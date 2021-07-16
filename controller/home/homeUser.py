
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid,login
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid

homeUser = Blueprint(name="homeUser", import_name=__name__)

@homeUser.route('/login', methods=['GET', 'POST'])
def login():
    page = 1
    PER_PAGE = 16
    if request.method == 'get':
        return redirect('/')
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        print('执行到此01')
        username = session.get('username')
        print('执行到此02')
        password = session.get('password')
    if username and password:
            if queryUserByname(username) != None:
              if DBSession.query(User).filter(User.username == username and User.password == password):
                username = session.get('username')
                userid = queryUserByname(username).userid
                goods1 = DBSession.query(Goods).filter(Goods.CTI >= 20).offset(page).limit(PER_PAGE)
                goods2 = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(
                PER_PAGE)
                count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
                pageination = Pagination(page, PER_PAGE, count)
                session['userid'] = userid
                return render_template('index.html', username=username, goods=goods1, goods2=goods2,
                                       pagination=pageination)
                if not goods1 and page != 1:
                    render_template('fshow.html', info="找不到这个网页")
              else:
                  return redirect('/')

            else:
                return redirect('/')

@homeUser.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['email'] = request.form['email']

        username = session.get('username')
        password = session.get('password')
        email = session.get('email')
        if username == ''or password == '':
            return "<script>alert('请输入用户名')</script>" and redirect('/')
        else:
            adduser1(username, password, email)
    if username == queryUserByname(username).username and password == queryUserByname(username).password:
        # queryUserByname(username) != None:
        return "注册成功" and redirect('/')
    else:
        return render_template('index.html')

@homeUser.route('/unregister')
def unregister():

    return render_template('index.html')


@homeUser.route('/selfinfo')
def selfinfo():
    if session.get('username') == None or session.get('username') == "":
        return redirect('/')
    else:
        username = session.get('username')
        user = queryUserByname(username)

        return render_template('selfinfo.html', user=user, userid=user.userid)

@homeUser.route('/adinfo')
def adinfo():
    if session.get('username') == None or session.get('username') == "":
        return redirect('/')
    else:
        username = session.get('username')
        user = queryUserByname(username)
        return render_template('adinfo.html', user=user, userid=user.userid)


@homeUser.route('/updeteUserinfo', methods=['GET', 'POST'])
def updeteUserinfo():
    if request.method == 'GET':
        if request.values.get('id') == None or request.values.get('id') == "":
            return redirect('/')
        else:
            userid = request.values.get('id')

            user = queryUserByid(userid).first()

        return render_template('updeteUserinfo.html', user=user, userid=userid)
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        proxyId = request.form['proxyId']
        integration = request.form['integration']

        users = DBSession.query(User).filter(User.username == username).first()
        if users!=None:
            users.username = username
            users.password = password
            users.email = email
            users.proxyId = proxyId
            users.integration = integration
            DBSession.commit()
            info = '用户增加成功'
            return render_template('fshow.html', info=info)
        else:
            return render_template('fshow.html', info="没有查询到任何用户")