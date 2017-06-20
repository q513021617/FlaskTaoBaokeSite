# -*- coding:utf-8 -*-
import xlrd
import mysql.connector
import os
# Open the workbook and define the worksheet


# 建立一个MySQL连接


def excle2sql():
    if os.path.exists('./upload/goods.xls'):
        book = xlrd.open_workbook("./upload/goods.xls")
        sheet = book.sheet_by_name("Page1")
        database = mysql.connector.connect(host="localhost", user="root", passwd="325602", db="caiweiwang")

        # 获得游标对象, 用于逐行遍历数据库数据
        cursor = database.cursor()

        # 创建插入SQL语句
        query = "insert into goods(goodsId, goodsName, goodsimage,goodsImAdr,goodsCla,TaokLink,goodPri, shopCount, CTI, Commission, dianzhuWW, dianzhuID, shopName, platClass,couponId, couponCount, CouponSurplus, CouponDenomination, CouponStart, CouponOver, CouponLink, CouponTKLink) values (%s, %s,%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s)"
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
        # 需要提前建好数据库的字段，再进行导入操作，每个字段对应一个表头

        for r in range(1, sheet.nrows):
            if sheet.cell(r, 8).value >= '20':
                goodsId = sheet.cell(r, 0).value
                goodsName = sheet.cell(r, 1).value
                goodsimage = sheet.cell(r, 2).value
                goodsImAdr = sheet.cell(r, 3).value
                goodsCla = sheet.cell(r, 4).value
                TaokLink = sheet.cell(r, 5).value
                goodPri = sheet.cell(r, 6).value
                shopCount = sheet.cell(r, 7).value
                CTI = sheet.cell(r, 8).value
                Commission = sheet.cell(r, 9).value
                dianzhuWW = sheet.cell(r, 10).value
                dianzhuID = sheet.cell(r, 11).value
                shopName = sheet.cell(r, 12).value
                platClass = sheet.cell(r, 13).value
                couponId = sheet.cell(r, 14).value
                couponCount = sheet.cell(r, 15).value
                CouponSurplus = sheet.cell(r, 16).value
                CouponDenomination = sheet.cell(r, 17).value
                CouponStart = sheet.cell(r, 18).value
                CouponOver = sheet.cell(r, 19).value
                CouponLink = sheet.cell(r, 20).value
                CouponTKLink = sheet.cell(r, 21).value

                values = (goodsId, goodsName, goodsimage, goodsImAdr, goodsCla, TaokLink, goodPri, shopCount, CTI, Commission, dianzhuWW, dianzhuID, shopName, platClass, couponId, couponCount, CouponSurplus, CouponDenomination, CouponStart, CouponOver, CouponLink, CouponTKLink)
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
        return ("你刚导入了 " + columns + " 列 and " + rows + " 行数据到MySQL!")
    else:
        return "这个文件不存在"
