# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger
from .tools import Base, DBSession, engine
from model.bill import queryBillbynumber
from model.income import queryincomeByNumber, addincome
from sqlalchemy import func
class User(Base):
    __tablename__ = 'user'
    userid = Column(BigInteger, primary_key=True)
    username = Column(String(20), unique=True, index=True)
    password = Column(String(128), unique=True, index=True)
    email = Column(String(64), unique=True, index=True)
    integration = Column(Integer, unique=False, index=True)
    proxyId = Column(BigInteger, unique=True, index=True)
    countBill = Column(BigInteger, unique=True, index=True)
    def __str__(self):
        return self

    def __int__(self, username, password, email, userid, integration):
        return


def deluserByid(userid):
    user = DBSession.query(User).filter(User.userid == userid).one()
    DBSession.delete(user)
    DBSession.commit()


def queryUserByid(userid):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(User).filter(User.userid == userid).first()
    # 关闭Session:
    return user


def queryUserByname(username):

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(User).filter(User.username == username).first()
    # 关闭Session:
    return user


def adduser1(username, password, email):
    # 创建新User对象:
    new_user = User( username=username, password=password, email=email, integration=0)
    # 添加到session:
    DBSession.add(new_user)
    # 提交即保存到数据库:
    DBSession.commit()


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return user


def queryUserScore(userid):
    score = DBSession.query(userid).first()
    return score


def appendproxyId(userid,proxyId):
    if(DBSession.query(User).filter(User.userid == userid).first().proxyId ==None ):
        DBSession.query(User).filter(User.userid == userid).update({User.proxyId: proxyId})
        DBSession.query(User).get(1)
        DBSession.commit()
        return 1
    else:
        return '你已经有一个上线会员了'


def addIntegration(userid, ordernumber):
    bill=queryBillbynumber(ordernumber)
    income = queryincomeByNumber(ordernumber)
    orderStatus = bill.orderStatus
    username = queryUserByid(userid).username
    if (bill != None):
        print('1')
        if (orderStatus == "订单结算"):
            print('2')
            if(income==None):
                addincome(userid, ordernumber, username)
                Integration = bill.payment * 10
                DBSession.query(User).filter(User.userid == userid).update({User.integration: User.integration+Integration})
                DBSession.query(User).get(1)
                DBSession.commit()
                return 1
            else:
                return "这个订单已经领过积分了"
        else:
            return "订单未结算"
    else:
        return "未找到该订单"


def count():
    n = DBSession.query(func.count(User.userid)).scalar()
    return n
