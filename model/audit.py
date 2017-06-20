# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger
from .tools import Base, DBSession, engine
from model.bill import queryBillbynumber
from model.income import queryincomeByNumber, addincome
from sqlalchemy import func
class Audit(Base):
    __tablename__ = 'audit'
    auditID = Column(BigInteger, primary_key=True)
    userid = Column(BigInteger, unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    telephone = Column(String(255), unique=True, index=True)

    def __str__(self):
        return self

    def __int__(self, auditID, userid,email,QQ,telephone):
        return


def delauditByid(auditID):
    audit = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
    DBSession.delete(audit)
    DBSession.commit()


def queryauditByid(auditID):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    audit = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
    # 关闭Session:
    return audit


def addadv(userid, username, email, telephone):
    # 创建新User对象:
    new_Audit = Audit(userid=userid, email=email, username=username, telephone=telephone)
    # 添加到session:
    DBSession.add(new_Audit)
    # 提交即保存到数据库:
    DBSession.commit()


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    Audit = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return Audit

