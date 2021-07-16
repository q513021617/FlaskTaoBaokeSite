
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.tools import and_
from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

homeNav = Blueprint(name="homeNav", import_name=__name__)

@homeNav.route('/Homedaily', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/Homedaily/page/<int:page>')
def Homedaily(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家日用%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家日用%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%美食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count, count2=count2,count4=count4,count5=count5,
                           count6=count6, count7=count7,count8=count8,count9=count9,Claname='居家日用')


@homeNav.route('/shoes', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/shoes/page/<int:page>')
def shoes(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()
        count3 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%母婴%')).count()
        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%鞋包配饰%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%美食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%文体车品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count3=count3,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9, Claname='女鞋')


@homeNav.route('/book', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/book/page/<int:page>')
def book(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
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
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='汽车用品')


@homeNav.route('/jiu', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/jiu/page/<int:page>')
def jiu(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodPri <=10).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodPri <=10).count()
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
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='九元包邮')


@homeNav.route('/charts', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/charts/page/<int:page>')
def charts(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).count()
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
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='抢卷排行')

@homeNav.route('/juanlive', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/juanlive/page/<int:page>')
def juanlive(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.couponCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.couponCount.desc()).count()
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
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='抢卷直播')


@homeNav.route('/searchmore', defaults={'page': 0}, methods=['GET', 'POST'])
@homeNav.route('/searchmore/page/<int:page>')
def searchmore(page):
    PER_PAGE = 32
    if request.method == 'POST':
        goodsname = request.form['goodsname']
        word=["%"+goodsname+"%"]
        goods = DBSession.query(Goods).filter(and_(Goods.goodsName.like(word), Goods.CTI >= 20)).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(and_(Goods.goodsName.like(word), Goods.CTI >= 20)).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        pageination = Pagination(page, PER_PAGE, count)
        return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2, count4=count4, count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9, Claname=goodsname)