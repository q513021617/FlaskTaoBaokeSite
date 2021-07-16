
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.bill import countO,Bill,addBill
from model.income import Income
from flask_paginate import Pagination, get_page_args
from common.decorator import login_required
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

orderAdmin = Blueprint(name="orderAdmin", import_name=__name__)
@orderAdmin.route('/searchorder/', defaults={'page': 0}, methods=['GET', 'POST'])
@orderAdmin.route('/searchorder/page/<int:page>')
@login_required()
def searchorder(page):
    PER_PAGE=15
    if request.method == 'GET':
        Bills = DBSession.query(Bill).offset(page).limit(PER_PAGE)
        count = DBSession.query(Bill).count()
        if not Bills and page != 1:
            abort(404)
    pageination = Pagination(page, PER_PAGE, count)
    return render_template('searchorder.html', Bills=Bills, pagination=pageination)

@orderAdmin.route('/showorder', methods=['GET', 'POST'])
@login_required()
def showorder():
    if request.method == 'GET':
        orderNumber = request.values.get('orderNumber')
        print(orderNumber)
        bill = DBSession.query(Bill).filter(Bill.orderNumber == orderNumber).first()
        print(bill.biilID)
        if bill==None:
            return render_template('show.html', info="没有这个账单的任何信息")
        else:
            return render_template('showorder.html', bill=bill)




@orderAdmin.route('/addorder')
@login_required()
def addorder():
    return render_template('addorder.html')