
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

homeBill = Blueprint(name="homeBill", import_name=__name__)

@homeBill.route('/Billsubmit', methods=['POST', 'GET'])
def Billsubmit():
    if request.method == 'POST':
        Billnumber = request.form['bill']
        username = session.get('username')
        userid = queryUserByname(username).userid
        print(Billnumber)
        print(username)
        print(userid)
        if DBSession.query(Bill).filter(Bill.orderStatus=='订单结账'):
            if queryBillbynumber(Billnumber)!=None and queryincomeByNumber(Billnumber)==None:
                intergration = queryBillbynumber(Billnumber).payment * 10
                addIntegration(userid, Billnumber)
                addincome(userid, Billnumber, username)
                return render_template('fshow.html', info='你已经成功入库订单,并且拿到了积分')
            elif queryBillbynumber(Billnumber)==None:
                return render_template('fshow.html', info='没有这个订单')
            elif queryincomeByNumber(Billnumber)!=None:
                return render_template('fshow.html', info='这个订单已经入库了!!')
            else:
                return render_template('selfinfo.html', info='没有成功拿到积分')
        else:
            return render_template('fshow.html', info='没有结账的订单不能入库!')
    if request.method == 'get':
        userid = session.get('userid')
        return render_template('/selfinfo.html', userid=userid)
