
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid
from flask_paginate import Pagination, get_page_args
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from common.decorator import login_required
from flask import Blueprint

useradmin = Blueprint(name="useradmin", import_name=__name__)

@useradmin.route('/searchuserbyName', methods=['get', 'post'])
@login_required()
def searchuserbyName():
    if request.method == 'POST':
        userName = request.form['searchName']
        print(userName)
        rs = DBSession.query(User).filter(User.username == userName).first()
        if (rs != None):
            page = 1
            users = DBSession.query(User).filter(User.username == userName)
            count = DBSession.query(User).filter(User.username == userName).count()
            if not users and page != 1:
                abort(404)
            pageination = Pagination(page, 1, count)

            return render_template('searchuser.html', users=users, pagination=pageination)
        else:
            erro = "没有找到该用户,,请正确输入用户名进行搜索!!"

            return render_template('show.html', info=erro)


@useradmin.route('/searchuser/', defaults={'page': 0}, methods=['GET', 'POST'])
@useradmin.route('/searchuser/page/<int:page>')
@login_required()
def searchuser(page):
    PER_PAGE = 15
    if request.method == 'GET':
        users = DBSession.query(User).offset(page).limit(PER_PAGE)
        count = DBSession.query(User).count()
        if not users and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('searchuser.html', users=users, pagination=pageination)


@useradmin.route('/deleteuser', methods=['GET', 'POST'])
@login_required()
def deleteuser():
    if request.method == 'GET':

        userid = request.values.get('userid')
        deluserByid(userid)
    return redirect("/searchuser")

@useradmin.route('/adduser', methods=['POST', 'GET'])
@login_required()
def adduser():
    if request.method == 'GET':
       return render_template('adduser.html')
    if request.method == 'POST':
        userid = request.form['userid']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        adduser1( username, password,email)
        info = '用户增加成功'
        return render_template('show.html', info=info)


@useradmin.route('/editsingleuser', methods=['GET', 'POST'])
@login_required()
def editsingleuser():
    if request.method == 'GET':
        userid = request.values.get('userid')
        user = queryUserByid(userid)
        return render_template('editsingleuser.html', user=user)
    if request.method == 'POST':

        usersid = request.form['usersid']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        integration =request.form['integration']
        proxyId = request.form['proxyId']
        user = DBSession.query(User).filter(User.userid == usersid).first()
        if user:
            user.usersid = usersid
            user.username = username
            user.password = password
            user.email = email
            user.integration = integration
            user.proxyId = proxyId
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)

@useradmin.route('/singleuser')
@login_required()
def singleuser():
    if request.method == 'GET':
        userid = request.values.get('userid')
        user = queryUserByid(userid)
        proxy = DBSession.query(Proxy).filter(Proxy.userid == userid).first()
        if proxy==None:
            return render_template('singleuser.html', user=user)
        else:
            a = proxy.proxyId
            print(a)
            n = queryVIPsbyId(proxy.proxyId).count()

            return render_template('singleuser.html', user=user, VIPNum=n)

