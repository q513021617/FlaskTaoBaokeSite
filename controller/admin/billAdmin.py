from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.income import queryincomeByNumber, addincome
from model.income import Income
from flask_paginate import Pagination, get_page_args
from model.bill import countO,Bill,addBill
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint
from common.decorator import login_required
from model.adv import Adv, queryAll
from model.UploadForm import UploadForm,set_mypic
billadmin = Blueprint(name="billadmin", import_name=__name__)


@billadmin.route('/Inputbills')
@login_required()
def Inputbills():
     print('正在执行')
     e = addBill()
     return render_template('show.html', info=e)


@billadmin.route('/deleteAllbill')
@login_required()
def deleteAllbill():
    e = DBSession.query(Bill)
    e.delete()
    DBSession.commit()
    return render_template('show.html', info='删除成功')

@billadmin.route('/uploadbill', methods=['GET', 'POST'])
@login_required()
def uploadbill():
    form = UploadForm()
    url = None
    if form.validate_on_submit():
        filename = form.upload.data.filename
        url = set_mypic.save(form.upload.data, name='bill.xls')
    return render_template('uploadorder.html', form=form, url=url)

@billadmin.route('/delbillExcel')
@login_required()
def delbillExcel():
    e = delexcel("./upload/bill.xls")
    return render_template('show.html', info=e)

@billadmin.route('/searchbillbyID', defaults={'page': 0}, methods=['GET', 'POST'])
@billadmin.route('/searchbillbyID/page/<int:page>')
@login_required()
def searchbillbyID(page):
    PER_PAGE=15
    if request.method == 'POST':
        bill = request.form['searchID']
        bill1 = DBSession.query(Bill).filter(Bill.orderNumber == bill).offset(page).limit(PER_PAGE)
        count = DBSession.query(Bill).filter(Bill.orderNumber == bill).count()
        if not bill and page != 1:
            abort(404)
        pageination = Pagination(page, PER_PAGE, count)

        return render_template('searchorder1.html', bill=bill1, pagination=pageination)
    else:
        erro = "没有找到商品,,请正确输入订单编号!"

        return render_template('show.html', info=erro)

@billadmin.route('/editsingleBills', methods=['GET', 'POST'])
@login_required()
def editsingleBills():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        bills = DBSession.query(Bill).filter(Bill.goodsid == goodsid).first()

        return render_template('editsingleBills.html', bills=bills)
    if request.method == 'POST':

        biilID = request.form['biilID']
        goodsid = request.form['goodsid']
        Payment = request.form['Payment']
        orderNumber = request.form['orderNumber']
        orderStatus=request.form['orderStatus']

        bills = DBSession.query(Bill).filter(Bill.goodsId == goodsid).first()
        if bills:
            bills.biilID = biilID
            bills.goodsid  = goodsid
            bills.Payment = Payment
            bills.orderNumber = orderNumber
            bills.orderStatus = orderStatus

            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)

@billadmin.route('/showBill/', defaults={'page': 1}, methods=['GET', 'POST'])
@billadmin.route('/showBill/page/<int:page>')
@login_required()
def showBill(page):
    PER_PAGE=15
    if request.method == 'GET':
        userId = request.values.get('usersid')

        income = DBSession.query(Income).filter(Income.userid == userId).offset(page).limit(PER_PAGE)
        count = DBSession.query(Income).filter(Income.userid == userId).count()
        if income==None:
            return render_template('show.html', info="这个会员没有任何账单")
        else:
            pageination = Pagination(page, PER_PAGE, count)
            return render_template('showBill.html', income=income, pagination=pageination)
