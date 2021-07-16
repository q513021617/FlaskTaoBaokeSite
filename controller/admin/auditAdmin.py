from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.audit import Audit
from model.audit import addadv
from common.decorator import login_required
from flask_paginate import Pagination, get_page_args
from model.bill import countO,Bill,addBill
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint
from model.adv import Adv, queryAll
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy

adminAudit = Blueprint(name="adminAudit", import_name=__name__)

@adminAudit.route('/auditAdmin', defaults={'page': 0}, methods=['GET', 'POST'])
@adminAudit.route('/auditAdmin/page/<int:page>')
@login_required()
def auditAdmin(page):
    PER_PAGE = 15
    if request.method == 'GET':
        audit = DBSession.query(Audit).offset(page).limit(PER_PAGE).all()
        count = DBSession.query(Audit).count()
        print(count)
        if not audit and page != 0:
            abort(404)
        pageination = Pagination(page, PER_PAGE, count)

    return render_template('proxyadmin.html', audit=audit, pagination=pageination)


@adminAudit.route('/searchaudit/', defaults={'page': 1}, methods=['GET', 'POST'])
@adminAudit.route('/searchaudit/page/<int:page>')
@login_required()
def searchaudit(page):
    PER_PAGE = 15
    if request.method == 'GET':
        username = request.values.get('username')
        audit = DBSession.query(Audit).filter(Audit.username == username).offset(page).limit(PER_PAGE)
        count = DBSession.query(Audit).filter(Audit.username == username).count()
        if not audit and page != 1:
            return render_template('show.html', info="没有找到目标,请输入正确的用户名搜索")
    pageination  = Pagination(page, PER_PAGE, audit)
    return render_template('searchaudit.html', audit=audit, pagination=pageination)



@adminAudit.route('/auditSucess', methods=['GET', 'POST'])
@login_required()
def auditSucess():
    if request.method == 'GET':
        auditID= request.values.get('auditID')
        a = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
        if a:
            addproxy(a.username, a.userid)
            DBSession.delete(a)
            DBSession.commit()
            return render_template('show.html', info="代理通过审核")
        else:
            return render_template('show.html', info="这个审核无效")
    else:
        return render_template('show.html', info="审核失败请重试")


@adminAudit.route('/auditDelete', methods=['GET', 'POST'])
@login_required()
def auditDelete():
    if request.method == 'GET':
        auditID= request.values.get('auditID')
        a = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
        DBSession.delete(a)
        DBSession.commit()
        return render_template('show.html', info="删除成功!")

    else:
        return render_template('show.html', info="删除失败!")