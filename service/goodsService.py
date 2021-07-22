from pymysql import Error, IntegrityError

from common.config import postData,getData
from model.goods import addgoods

currentpage=1
tottalpage=0
def getGoodsList():
        version = 'v1.2.4'  # 当前版本号
        url = 'http://openapi.dataoke.com/api/goods/get-goods-list'
        data = {'pageId': 1, 'version': version}
        response = getData(url, data)
        goodslist=response['data']['list']
        return goodslist


def getGoodsListByTime(page):
    version = 'v1.2.4'  # 当前版本号
    url = 'http://openapi.dataoke.com/api/goods/pull-goods-by-time'
    data = {'pageId': page, 'version': version}
    response = getData(url, data)
    goodslist = response['data']['list']
    globals()['tottalpage'] = response['data']['totalNum']
    globals()['currentpage'] = response['data']['pageId']
    return goodslist

def batchInsertGoods(page):
       goodslist = getGoodsListByTime(page)
       for item in goodslist:
           try:
               addgoods(item["goodsId"], item["title"], item["mainPic"], "", item["actualPrice"],
                         item["commissionRate"], item["mainPic"], item["couponLink"], item["itemLink"],
                         item["monthSales"], item["couponReceiveNum"])
               print("导入商品中====商品ID "+item["goodsId"])
           except IntegrityError as err:
                print(err)
           finally:
               continue

def getAllGoodsToDBByTime():
    batchInsertGoods(1)
    for i in range(2,tottalpage):
        batchInsertGoods(currentpage)
# batchInsertGoods()
# getAllGoodsToDBByTime()