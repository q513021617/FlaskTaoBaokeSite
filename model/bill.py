# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String,BigInteger,Float
from model.tools import Base, DBSession, engine
from sqlalchemy import func
import mysql.connector
import xlrd


class Bill(Base):
    __tablename__ = 'bill'
    biilID = Column(BigInteger, primary_key=True)
    goodsid = Column(String(255), unique=True, index=True)
    payment = Column(Float(255), unique=False, index=True)
    orderNumber = Column(BigInteger, unique=True, index=True)
    orderStatus = Column(String(255), unique=False, index=True)

    def __str__(self):
        return self

    def __int__(self, goodsid, payment,orderNumber, oderStatus):
        return


def delbillBynumber(orderNumber):
    bill = DBSession.query(Bill).filter(Bill.orderNumber == orderNumber).one()
    DBSession.delete(bill)
    DBSession.commit()


def queryBillbynumber(orderNumber):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    bill = DBSession.query(Bill).filter(Bill.orderNumber == orderNumber).first()
    # 关闭Session:
    return bill


def addBill():
    # 创建新User对象:
    book = xlrd.open_workbook("./upload/bill.xls")
    sheet = book.sheet_by_name("Page1")
    database = mysql.connector.connect(host="localhost", user="root", passwd="325602", db="caiweiwang")
    cursor = database.cursor()

    # 创建插入SQL语句
    query = "insert into bill(goodsid, Payment, orderNumber,orderStatus) values (%s, %s,%s,%s)"
    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
    # 需要提前建好数据库的字段，再进行导入操作，每个字段对应一个表头

    for r in range(1, sheet.nrows):
        goodsid = sheet.cell(r, 3).value
        orderStatus = sheet.cell(r, 8).value
        Payment = sheet.cell(r, 12).value
        orderNumber = sheet.cell(r, 24).value
        values = (goodsid, Payment, orderNumber,orderStatus)
        # 执行sql语句
        cursor.execute(query, values)

     # 关闭游标
    cursor.close()

    # 提交
    database.commit()

    # 关闭数据库连接
    database.close()

    # 打印结果

    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    return ("你刚导入了订单数据 " + columns + " 列 and " + rows + " 行数据到MySQL!")


def queryAll(cls):
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(cls).all()
    # 关闭Session:
    session.close()
    return user


def countO():
    n = DBSession.query(func.count(Bill.biilID)).scalar()
    return n