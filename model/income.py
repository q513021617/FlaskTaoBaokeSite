# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger
from .tools import Base, DBSession, engine


class Income(Base):
    __tablename__ = 'income'
    incomId = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, unique=True, index=True)
    username = Column(String(20), unique=True,index=True)
    orderNumber = Column(String(500), unique=True, index=True)

    def __str__(self):
        return self

    def __int__(self, incomId, userid, orderNumber):
        return


def delincomeByid(incomId):
    income = DBSession.query(Income).filter(Income.incomId == incomId).first()
    DBSession.delete(income)
    DBSession.commit()


def queryincomeByNumber(orderNumber):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    income = DBSession.query(Income).filter(Income.orderNumber == orderNumber).first()
    # 关闭Session:
    return income


def queryincomeByname(username):

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    income = DBSession.query(Income).filter(Income.username == username).one()
    # 关闭Session:
    return income


def addincome(userid,orderNumber,username):
    # 创建新User对象:
    new_income = Income( userid=userid, orderNumber=orderNumber, username=username)
    # 添加到session:
    DBSession.add(new_income)
    # 提交即保存到数据库:
    DBSession.commit()


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return user
