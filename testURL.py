from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid
from model.bill import countO,Bill,addBill
from wtforms import SubmitField
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy
from flask_wtf import FlaskForm
from flask_paginate import Pagination, get_page_args
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES,EXECUTABLES,configure_uploads,patch_request_class
from model.excle2sql import excle2sql
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from model.goods import queryGoodByid, updategoodsById,addgoods1, delGoodsByid
from model.income import Income
from model.adv import Adv, queryAll
from model.audit import Audit
import time
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
'''''''''
class Item():
    clicked = False
    num = 0


items_count = int(count // 10.0)
items = []
if items_count > 10:
    items_count = 10
for i in range(items_count):
    item = Item()
    if i == 0:
        item.clicked = True
    item.num = i
    items.append(item)
return render_template('searchgoods.html', goods=goods, items=items)
elif request.method == 'POST':
offset = request.get_data('offset')
goods = DBSession.query(Goods).offset(offset).limit(10)
'''''''''