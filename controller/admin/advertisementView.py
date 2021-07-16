from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint
from model.adv import Adv, queryAll

advadmin = Blueprint(name="advadmin", import_name=__name__)

@advadmin.route('/adadmin/', defaults={'page': 0}, methods=['GET', 'POST'])
@advadmin.route('/admin/page/<int:page>')
def adadmin(page):
    PER_PAGE = 15
    if request.method == 'GET':
        Adv1 = DBSession.query(Adv).offset(page).limit(PER_PAGE)
        count = DBSession.query(Adv).count()
        if not Adv1 and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('adadmin.html', Adv=Adv1, pagination=pageination)

@advadmin.route('/editsingleadv', methods=['GET', 'POST'])
def editsingleadv():
    if request.method == 'GET':
        adID = request.values.get('adID')
        print(adID)
        adv1 = DBSession.query(Adv).filter(Adv.adID == adID).first()
        return render_template('editsingleadv.html', adv1=adv1)
    if request.method == 'POST':

        advId = request.form['advId']
        advaddress = request.form['advaddress']
        advlink = request.form['advlink']
        adname = request.form['adname']
        Adv1 = DBSession.query(Adv).filter(Adv.adID == advId).first()
        if Adv1:
            Adv1.adID = advId
            Adv1.advaddress = advaddress
            Adv1.advlink = advlink
            Adv1.adname = adname
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)