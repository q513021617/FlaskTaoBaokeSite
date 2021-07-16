from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.bill import countO,Bill,addBill
from model.proxy import queryAll, Proxy
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid,login

from flask import Blueprint
from model.UploadForm import UploadForm
from common.decorator import login_required
from model.adv import Adv, queryAll

indexadmin = Blueprint(name="indexadmin", import_name=__name__)


@indexadmin.route('/')
@login_required()
def index():
    n = count()
    g = countG()
    o = countO()
    P = queryAll(Proxy)
    return render_template('adminIndex.html', countuser=n, countgoods=g, countorder=o, proxy=P)

@indexadmin.route('/quitlogin', methods=['GET', 'POST'])
@login_required()
def quitlogin():
    if request.method == 'GET':
       session.pop("username")
       return redirect("/admin")


@indexadmin.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
       return render_template('adminLogin.html')
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       if(login(username, password)):
           session["username"]=username
           return redirect("/admin")
       return render_template("adminLogin.html")
