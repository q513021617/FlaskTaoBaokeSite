
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.bill import countO,Bill,addBill
from model.income import Income
from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

homeOrder = Blueprint(name="homeOrder", import_name=__name__)




