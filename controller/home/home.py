
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

home = Blueprint(name="home", import_name=__name__)

@home.route('/', defaults={'page': 0}, methods=['GET', 'POST'])
@home.route('/page/<int:page>')
def hello(page):
    PER_PAGE = 16
    if request.method == 'GET':
        goods1 = DBSession.query(Goods).filter(Goods.CTI >= 20).offset(page).limit(PER_PAGE)
        goods2 = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
        if not goods1 and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods1, pagination=pageination, goods2=goods2)
    username = session.get('username')
    return render_template('index.html', username=username, goods=goods1, goods2=goods2,pagination=pageination)
