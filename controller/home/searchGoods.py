from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args
from model.tools import and_
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

search = Blueprint(name="search", import_name=__name__)

@search.route('/girlwear', defaults={'page': 1}, methods=['GET', 'POST'])
@search.route('/girlwear/page/<int:page>')
def girlwear(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='女装')


@search.route('/motherbaby', defaults={'page': 1}, methods=['GET', 'POST'])
@search.route('/motherbaby/page/<int:page>')
def motherbaby(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%婴儿装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%婴儿装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count, count2=count2, count4=count4, count5=count5,
                           count6=count6, count7=count7, count8=count8, count9=count9, Claname='婴儿装')


@search.route('/boywear', defaults={'page': 1}, methods=['GET', 'POST'])
@search.route('/boywear/page/<int:page>')
def boywear(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%男装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%男装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='男装')


@search.route('/foods', defaults={'page': 1}, methods=['GET', 'POST'])
@search.route('/foods/page/<int:page>')
def foods(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='零食')

@search.route('/singlepage', defaults={'page': 1}, methods=['GET', 'POST'])
@search.route('/singlepage/page/<int:page>')
def singlepage(page):
    PER_PAGE = 8
    if request.method == 'GET':
        goodsid=request.values.get('goodsid')

        goods = DBSession.query(Goods).filter(Goods.goodsId == goodsid).first()
        goods1 = DBSession.query(Goods).filter(and_(Goods.CTI >= 20, Goods.goodsCla == goods.goodsCla)).offset(page).limit(
            PER_PAGE)
        count = DBSession.query(Goods).filter(and_(Goods.CTI >= 20, Goods.goodsCla == goods.goodsCla)).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('singlepage.html', goods=goods, pagination=pageination,goods1=goods1)
    return render_template('singlepage.html', username=session.get('username'), goods=goods, pagination=pageination,goods1=goods1)