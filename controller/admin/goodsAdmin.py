from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args
from flask_bootstrap import Bootstrap
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.goods import queryGoodByid, addgoods1, delGoodsByid
from model.pages import Pagination
from flask import Blueprint
from model.UploadForm import UploadForm

from model.adv import Adv, queryAll
from flask_uploads import UploadSet, IMAGES,configure_uploads
# from caiweiwang import app
from model.excle2sql import excle2sql
from common.decorator import login_required
from service.goodsService import getAllGoodsToDBByTime
set_mypic = UploadSet('mypic')
# bootstrap = Bootstrap(app)
# app.config['UPLOADED_MYPIC_DEST'] = './upload'
# app.config['UPLOADED_MYPIC_ALLOW'] = IMAGES
# configure_uploads(app, set_mypic)
# app.config['SECRET_KEY'] = 'xxxxx'

goodsadmin = Blueprint(name="goodsadmin", import_name=__name__)


@goodsadmin.route('/uploadgoods', methods=['GET', 'POST'])
@login_required()
def uploadgoods():
    form = UploadForm()
    url = None
    if form.validate_on_submit():
        filename = form.upload.data.filename
        url = set_mypic.save(form.upload.data, name='goods.xls')
    return render_template('uploadgoods.html', form=form, url=url)





@goodsadmin.route('/addgoods', methods=['POST', 'GET'])
@login_required()
def addgoods():
    if request.method == 'GET':
       return render_template('addgoods.html')
    if request.method == 'POST':
        goodsid = request.form['goodsId']
        goodsname = request.form['goodsname']
        goodsimage = request.form['goodsimage']
        goodsCla = request.form['goodsCla']
        goodsPri = request.form['goodsPri']
        CTI = request.form['CTI']
        goodsImAdr = request.form['goodsImAdr']
        addgoods1(goodsid, goodsname, goodsimage, goodsCla, goodsPri, CTI, goodsImAdr)
        info = '商品增加成功'
        return render_template('show.html', info=info)

@goodsadmin.route('/Inputgoods')
@login_required()
def Inputgoods():
     print('正在执行')
     e = excle2sql()
     return render_template('show.html', info=e)

@goodsadmin.route('/delgoodExcel')
@login_required()
def delgoodExcel():
    e = delexcel("./upload/goods.xls")
    return render_template('show.html', info=e)


@goodsadmin.route('/deleteAllgoods')
@login_required()
def delgoods():
    e = DBSession.query(Goods)
    e.delete()
    DBSession.commit()
    return render_template('show.html', info='删除成功')


@goodsadmin.route('/editsinglegoods', methods=['GET', 'POST'])
@login_required()
def editsinglegoods():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        goods = queryGoodByid(goodsid)
        return render_template('editsinglegoods.html', goods=goods)
    if request.method == 'POST':

        goodsid = request.form['goodsId']
        goodsname = request.form['goodsname']
        goodsimage = request.form['goodsimage']
        goodsCla = request.form['goodsCla']
        goodsPri =request.form['goodsPri']
        CTI = request.form['CTI']
        goodsImAdr = request.form['goodsImAdr']
        goods = DBSession.query(Goods).filter(Goods.goodsId == goodsid).first()
        if goods:
            goods.goodsName = goodsname
            goods.goodsimage = goodsimage
            goods.goodsCla = goodsCla
            goods.goodPri = goodsPri
            goods.CTI = CTI
            goods.goodsImAdr = goodsImAdr
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)

@goodsadmin.route('/singlegoods')
@login_required()
def singlegoods():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        goods = queryGoodByid(goodsid)
        return render_template('singlegoods.html', goods=goods)

@goodsadmin.route('/batchGetGoods')
@login_required()
def batchGetGoods():
    if request.method == 'GET':
        getAllGoodsToDBByTime()
        return {"status" : True,"data":{}}

@goodsadmin.route('/searchgoodbyID', methods=['GET', 'POST'])
def searchgoodbyID():
    if request.method == 'POST':
        goodsId = request.form['searchID']
        print(goodsId)
        rs = DBSession.query(Goods).filter(Goods.goodsId == goodsId).first()
        if( rs!=None):
            page = 1
            goods = DBSession.query(Goods).filter(Goods.goodsId == goodsId)
            count = DBSession.query(Goods).filter(Goods.goodsId == goodsId).count()
            if not goods and page != 1:
                abort(404)
            pageination = Pagination(page, 1, count)

            return render_template('searchgoods.html', goods=goods, pagination=pageination)
        else:
            erro = "没有找到商品,,请正确输入商品ID!!"

            return render_template('show.html', info=erro)

@goodsadmin.route('/searchgoods/', defaults={'page': 0}, methods=['GET', 'POST'])
@goodsadmin.route('/searchgoods/page/<int:page>')
@login_required()
def searchgoods(page):
    PER_PAGE = 15
    if request.method == 'GET':
        goods = DBSession.query(Goods).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
        if not goods and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('searchgoods.html', goods=goods, pagination=pageination)


@goodsadmin.route('/deletegoods', methods=['GET', 'POST'])
@login_required()
def deletegoods():
    if request.method == 'GET':

        goodsid = request.values.get('goodsid')
        print(goodsid)
        delGoodsByid(goodsid)
    return redirect("/searchgoods")