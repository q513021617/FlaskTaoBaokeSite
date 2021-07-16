from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy
from flask import Blueprint
from wtforms import SubmitField
from common.decorator import login_required
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid
from flask_uploads import UploadSet, IMAGES,configure_uploads


set_mypic = UploadSet('mypic')


adminProxy = Blueprint(name="adminProxy", import_name=__name__)


@adminProxy.route('/deleteproxy', methods=['GET', 'POST'])
@login_required()
def deleteproxy():
    if request.method == 'GET':
        proxyId = request.values.get('proxyid')
        print(proxyId)
        delproxyByid(proxyId)
    return redirect("/")


@adminProxy.route('/singleproxy')
@login_required()
def singleproxy():
    if request.method == 'GET':
        proxyid = request.values.get('proxyid')
        print(proxyid)
        proxy = queryProxyByid(proxyid)
        if proxy==None:
            return render_template('show.html', info="没有这个代理信息!")
        else:
            a = proxy.proxyId
            print(a)
            n = DBSession.query(User).filter(User.proxyId == a).count()
        return render_template('singleproxy.html', proxy=proxy, VIPNum=n)