
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG

from flask_paginate import Pagination, get_page_args

from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from flask import Blueprint

homeError = Blueprint(name="homeError", import_name=__name__)

@homeError.route('/500')
def error():
    return render_template('500.html')


@homeError.route('/404')
def error404():
    return render_template('error.html')
