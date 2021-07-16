# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,and_,Float
from model.tools import Base, DBSession

class Goods(Base):
    __tablename__ = 'goods'
    goodsId = Column(String(64), primary_key=True)
    goodsName = Column(String(64))
    goodsimage = Column(String(128))
    goodsImAdr = Column(String(64))
    goodsCla = Column(String(64))
    TaokLink = Column(String(64))
    goodPri = Column(String(128))
    shopCount = Column(String(64))
    CTI = Column(Float(24))
    Commission = Column(String(64))
    dianzhuWW = Column(String(128))
    dianzhuID = Column(String(64))
    shopName = Column(String(64))
    platClass = Column(String(64))
    couponId = Column(String(128))
    couponCount = Column(String(64))
    CouponSurplus = Column(Integer)
    CouponDenomination = Column(String(64))
    CouponStart = Column(String(128))
    CouponOver = Column(String(64))
    CouponLink = Column(String(128))
    CouponTKLink = Column(String(128))

    def __str__(self):
        return self

    def __int__(self, goodsId, goodsName, goodsimage):
        return


def delGoodsByid(Goodsid):
    goods = DBSession.query(Goods).filter(Goods.goodsId == Goodsid).one()

    DBSession.delete(goods)
    DBSession.commit()


def queryGoodByid(Goodsid):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    goods = DBSession.query(Goods).filter(Goods.goodsId == Goodsid).first()
    # 关闭Session:
    return goods


def queryCouponCountById(Goodsid):

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    goods = DBSession.query(Goods).filter(Goods.goodsid == Goodsid).one()
    # 关闭Session:
    return goods


def queryGoodsByType(GoodCla):
    words = ['%'+GoodCla+'%']
    rule = and_(*[Goods.goodsCla.like(w) for w in words])
    goods = DBSession.query(Goods).filter(rule)
    return goods


def addgoods1(goodsid, goodsname, goodsimage, goodsCla, goodsPri, CTI, goodsImAdr):
    # 创建新User对象:
    new_goods = Goods(goodsId=goodsid, goodsName=goodsname, goodsimage=goodsimage, goodPri=goodsPri, goodsCla=goodsCla,CTI=CTI,goodsImAdr=goodsImAdr)
    # 添加到session:
    DBSession.add(new_goods)
    # 提交即保存到数据库:
    DBSession.commit()

def count2():
    count = DBSession.count()

def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    goods = session.query(cls).all()
    # 关闭Session:
    session.close()
    return goods

def updategoodsById(goodsid,goodsname,goodsimage,goodsCla,goodsPri,CTI,goodsImAdr):
    DBSession.query(Goods).filter(Goods.goodsId == goodsid).update({goodsname: goodsname,goodsimage:goodsimage})
    DBSession.query(Goods).get(2)
    DBSession.commit()
    return '更新成功'



def countG():
    n = DBSession.query(Goods).count()
    return n