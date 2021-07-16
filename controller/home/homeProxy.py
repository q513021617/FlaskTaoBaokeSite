from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint
from model.audit import addadv
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid
homeProxy = Blueprint(name="homeProxy", import_name=__name__)



@homeProxy.route('/showVIP')
def showVIP():
    if request.method == 'GET':
        proxyId = request.values.get('proxyId')
        number = request.values.get('vip')

        user = DBSession.query(User).filter(User.proxyId == proxyId).all()
        if user==None or number < '1':
            return render_template('show.html', info="这个代理没有任何下线")
        else:
            return render_template('showVIP.html', user=user)

@homeProxy.route('/adproxy', methods=['GET', 'POST'])
def adproxy():
    if request.method == 'GET':
        username = session.get('username')
        a = DBSession.query(Proxy).filter(Proxy.username == username).all()
        if username == None:
            return render_template('fshow.html', info='请登录之后再来这个模块')
        elif a:
            userid = request.values.get('userid')
            p = DBSession.query(Proxy).filter(Proxy.userid == userid).first()
            countB = DBSession.query(User).filter(User.proxyId == p.proxyId).count()
            countP = DBSession.query(User.userid).filter(User.proxyId == p.proxyId).count()
            return render_template('adproxy.html', countB=countB, countP=countP)
        else:
            return render_template('fshow.html', info='你还不是代理不能进入这个模块')



@homeProxy.route('/applyproxy', methods=['GET', 'POST'])
def applyproxy():
    if request.method == 'GET':
        return render_template('applyproxy.html')
    if request.method == 'POST':
        username = request.form.get('username')
        userid = session.get('userid')
        email = request.form.get('email')
        telephone = request.form.get('telephone')

        addadv(userid, username, email, telephone)
        return render_template('fshow.html', info="申请成功!请等待管理员回复")