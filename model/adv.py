# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger
from .tools import Base, DBSession, engine
from model.bill import queryBillbynumber
from model.income import queryincomeByNumber, addincome
from sqlalchemy import func
class Adv(Base):
    __tablename__ = 'Advertisement'
    adID = Column(BigInteger, primary_key=True)
    advaddress = Column(String(255), unique=True, index=True)
    advlink = Column(String(255), unique=True, index=True)
    adname = Column(String(255), unique=True, index=True)
    def __str__(self):
        return self

    def __int__(self, adID, advaddress, advlink):
        return


def deladvByid(adID):
    adv = DBSession.query(Adv).filter(Adv.adID == adID).first()
    DBSession.delete(adv)
    DBSession.commit()


def queryadvByid(adID):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    adv = DBSession.query(Adv).filter(Adv.adID == adID).first()
    # 关闭Session:
    return adv


def addadv(adID, advaddress, advlink):
    # 创建新User对象:
    new_Adv = Adv(adID=adID, advaddress=advaddress, advlink=advlink)
    # 添加到session:
    DBSession.add(new_Adv)
    # 提交即保存到数据库:
    DBSession.commit()


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    adv = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return adv

