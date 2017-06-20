# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer, create_engine,text,and_
from sqlalchemy.orm import sessionmaker, scoped_session, session
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import _include_sqlalchemy, SQLAlchemy

import os
# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:325602@localhost:3306/caiweiwang?charset=utf8')
# 创建DBSession类型:

DBSession = scoped_session(sessionmaker(bind=engine))


def delexcel(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            return '刪除成功'
        else:
            return "这个文件不存在!"


def isfile(path):
    return os.path.isfile(path)


def deleteTable(table):
    Sesson = sessionmaker(bind=engine)
    sesson = Sesson()
    x = sesson.query(table).from_statement(text("select * from goods")).all()
    sesson.delete(x)
    return "删除成功"