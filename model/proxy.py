# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger
from .tools import Base, DBSession, engine
from model.user import queryUserByid,User

class Proxy(Base):
    __tablename__ = 'proxy'
    proxyId = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, unique=True, index=True)
    username = Column(String(20), unique=True, index=True)
    income = Column(String(64), unique=True, index=True)

    def __str__(self):
        return self

    def __int__(self, username, password, email, userid, integration):
        return


def delproxyByid(proxyId):
    proxy = DBSession.query(Proxy).filter(Proxy.proxyId == proxyId).first()
    DBSession.delete(proxy)
    DBSession.commit()


def queryProxyByid(proxyId):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    proxy = DBSession.query(Proxy).filter(Proxy.proxyId == proxyId).first()
    # 关闭Session:
    return proxy



def queryProxyByname(username):

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    proxy = DBSession.query(Proxy).filter(Proxy.username == username).one()
    # 关闭Session:
    return proxy


def addproxy(username, userid):
    # 创建新User对象:
    new_user = Proxy(username=username, userid=userid)
    # 添加到session:
    DBSession.add(new_user)
    # 提交即保存到数据库:
    DBSession.commit()


def queryVIPsbyId(proxyId):
    VIPs = DBSession.query(User).filter(User.proxyId == proxyId).all()
    return VIPs


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return user
