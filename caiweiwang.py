from flask import Flask, render_template, redirect, url_for, session, request
from model.tools import DBSession,and_
from model.goods import Goods
from model.user import queryUserByname,queryUserByid
app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'  # session会话必备
from model.bill import queryBillbynumber,Bill
from model.income import queryincomeByNumber, addincome
from model.user import addIntegration, adduser1, User
from model.pages import Pagination
from model.audit import addadv,Audit
from model.proxy import Proxy
from flask import Flask, render_template, redirect, url_for, session, request,flash,abort
from model.goods import queryAll, Goods, countG
from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid
from model.bill import countO,Bill,addBill
from wtforms import SubmitField
from model.proxy import queryAll, Proxy,queryVIPsbyId,queryProxyByid,delproxyByid,addproxy
from flask_wtf import FlaskForm
from flask_paginate import Pagination, get_page_args
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES,EXECUTABLES,configure_uploads,patch_request_class
from model.excle2sql import excle2sql
from model.tools import delexcel, DBSession,isfile,deleteTable
from model.pages import Pagination
from model.goods import queryGoodByid, updategoodsById,addgoods1, delGoodsByid
from model.income import Income
from model.adv import Adv, queryAll
from model.audit import Audit


@app.route('/', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/page/<int:page>')
def hello(page):
    PER_PAGE = 16
    if request.method == 'GET':
        goods1 = DBSession.query(Goods).filter(Goods.CTI >= 20).offset(page).limit(PER_PAGE)
        goods2 = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
        if not goods1 and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods1, pagination=pageination, goods2=goods2)
    username = session.get('username')
    return render_template('index.html', username=username, goods=goods1, goods2=goods2,pagination=pageination)


@app.route('/singlepage', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/singlepage/page/<int:page>')
def singlepage(page):
    PER_PAGE = 8
    if request.method == 'GET':
        goodsid=request.values.get('goodsid')

        goods = DBSession.query(Goods).filter(Goods.goodsId == goodsid).first()
        goods1 = DBSession.query(Goods).filter(and_(Goods.CTI >= 20, Goods.goodsCla == goods.goodsCla)).offset(page).limit(
            PER_PAGE)
        count = DBSession.query(Goods).filter(and_(Goods.CTI >= 20, Goods.goodsCla == goods.goodsCla)).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('singlepage.html', goods=goods, pagination=pageination,goods1=goods1)
    return render_template('singlepage.html', username=session.get('username'), goods=goods, pagination=pageination,goods1=goods1)


@app.route('/girlwear', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/girlwear/page/<int:page>')
def girlwear(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='女装')


@app.route('/motherbaby', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/motherbaby/page/<int:page>')
def motherbaby(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%婴儿装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%婴儿装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count, count2=count2, count4=count4, count5=count5,
                           count6=count6, count7=count7, count8=count8, count9=count9, Claname='婴儿装')


@app.route('/boywear', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/boywear/page/<int:page>')
def boywear(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%男装%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%男装%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='男装')


@app.route('/foods', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/foods/page/<int:page>')
def foods(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='零食')




set_mypic = UploadSet('mypic')
bootstrap = Bootstrap(app)
app.config['UPLOADED_MYPIC_DEST'] = './upload'
app.config['UPLOADED_MYPIC_ALLOW'] = IMAGES
configure_uploads(app, set_mypic)
app.config['SECRET_KEY'] = 'xxxxx'





@app.route('/searchuser/', defaults={'page': 0}, methods=['GET', 'POST'])
@app.route('/searchuser/page/<int:page>')
def searchuser(page):
    PER_PAGE = 15
    if request.method == 'GET':
        users = DBSession.query(User).offset(page).limit(PER_PAGE)
        count = DBSession.query(User).count()
        if not users and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('searchuser.html', users=users, pagination=pageination)


@app.route('/searchuserbyName', methods=['get', 'post'])
def searchuserbyName():
    if request.method == 'POST':
        userName = request.form['searchName']
        print(userName)
        rs = DBSession.query(User).filter(User.username == userName).first()
        if (rs != None):
            page = 1
            users = DBSession.query(User).filter(User.username == userName)
            count = DBSession.query(User).filter(User.username == userName).count()
            if not users and page != 1:
                abort(404)
            pageination = Pagination(page, 1, count)

            return render_template('searchuser.html', users=users, pagination=pageination)
        else:
            erro = "没有找到该用户,,请正确输入用户名进行搜索!!"

            return render_template('show.html', info=erro)


@app.route('/adadmin/', defaults={'page': 0}, methods=['GET', 'POST'])
@app.route('/admin/page/<int:page>')
def adadmin(page):
    PER_PAGE = 15
    if request.method == 'GET':
        Adv1 = DBSession.query(Adv).offset(page).limit(PER_PAGE)
        count = DBSession.query(Adv).count()
        if not Adv1 and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('adadmin.html', Adv=Adv1, pagination=pageination)


@app.route('/uploadgoods', methods=['GET', 'POST'])#1
def uploadgoods():
    form = UploadForm()
    url = None
    if form.validate_on_submit():
        filename = form.upload.data.filename
        url = set_mypic.save(form.upload.data, name='goods.xls')
    return render_template('uploadgoods.html', form=form, url=url)


class UploadForm(FlaskForm):
    # 文件field设置为‘必须的’，过滤规则设置为‘set_mypic’
    upload = FileField('image', validators=[FileRequired(), FileAllowed(set_mypic, 'you can upload images only!')])
    submit = SubmitField('ok')


@app.route('/Inputgoods')
def Inputgoods():
     print('正在执行')
     e = excle2sql()
     return render_template('show.html', info=e)


@app.route('/Inputbills')
def Inputbills():
     print('正在执行')
     e = addBill()
     return render_template('show.html', info=e)


@app.route('/delgoodExcel')
def delgoodExcel():
    e = delexcel("./upload/goods.xls")
    return render_template('show.html', info=e)


@app.route('/deleteAllgoods')
def delgoods():
    e = DBSession.query(Goods)
    e.delete()
    DBSession.commit()
    return render_template('show.html', info='删除成功')


@app.route('/deleteAllbill')
def deleteAllbill():
    e = DBSession.query(Bill)
    e.delete()
    DBSession.commit()
    return render_template('show.html', info='删除成功')




@app.route('/searchgoodbyID', methods=['GET', 'POST'])
def searchgoodbyID():
    if request.method == 'POST':
        goodsId = request.form['searchID']
        print(goodsId)
        rs = DBSession.query(Goods).filter(Goods.goodsId == goodsId).first()
        if( rs!=None):
            page = 1
            goods = DBSession.query(Goods).filter(Goods.goodsId == goodsId)
            count = DBSession.query(Goods).filter(Goods.goodsId == goodsId).count()
            if not goods and page != 1:
                abort(404)
            pageination = Pagination(page, 1, count)

            return render_template('searchgoods.html', goods=goods, pagination=pageination)
        else:
            erro = "没有找到商品,,请正确输入商品ID!!"

            return render_template('show.html', info=erro)


@app.route('/searchgoods/', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/searchgoods/page/<int:page>')
def searchgoods(page):
    PER_PAGE = 15
    if request.method == 'GET':
        goods = DBSession.query(Goods).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
        if not goods and page != 1:
            abort(404)
    pageination  = Pagination(page, PER_PAGE, count)
    return render_template('searchgoods.html', goods=goods, pagination=pageination)


@app.route('/auditAdmin', defaults={'page': 0}, methods=['GET', 'POST'])
@app.route('/auditAdmin/page/<int:page>')
def auditAdmin(page):
    PER_PAGE = 15
    if request.method == 'GET':
        audit = DBSession.query(Audit).offset(page).limit(PER_PAGE).all()
        count = DBSession.query(Audit).count()
        print(count)
        if not audit and page != 0:
            abort(404)
        pageination = Pagination(page, PER_PAGE, count)

    return render_template('proxyadmin.html', audit=audit, pagination=pageination)


@app.route('/searchaudit/', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/searchaudit/page/<int:page>')
def searchaudit(page):
    PER_PAGE = 15
    if request.method == 'GET':
        username = request.values.get('username')
        audit = DBSession.query(Audit).filter(Audit.username == username).offset(page).limit(PER_PAGE)
        count = DBSession.query(Audit).filter(Audit.username == username).count()
        if not audit and page != 1:
            return render_template('show.html', info="没有找到目标,请输入正确的用户名搜索")
    pageination  = Pagination(page, PER_PAGE, audit)
    return render_template('searchaudit.html', audit=audit, pagination=pageination)



@app.route('/auditSucess', methods=['GET', 'POST'])
def auditSucess():
    if request.method == 'GET':
        auditID= request.values.get('auditID')
        a = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
        if a:
            addproxy(a.username, a.userid)
            DBSession.delete(a)
            DBSession.commit()
            return render_template('show.html', info="代理通过审核")
        else:
            return render_template('show.html', info="这个审核无效")
    else:
        return render_template('show.html', info="审核失败请重试")







@app.route('/auditDelete', methods=['GET', 'POST'])
def auditDelete():
    if request.method == 'GET':
        auditID= request.values.get('auditID')
        a = DBSession.query(Audit).filter(Audit.auditID == auditID).first()
        DBSession.delete(a)
        DBSession.commit()
        return render_template('show.html', info="删除成功!")

    else:
        return render_template('show.html', info="删除失败!")




def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page


@app.route('/deletegoods', methods=['GET', 'POST'])
def deletegoods():
    if request.method == 'GET':

        goodsid = request.values.get('goodsid')
        print(goodsid)
        delGoodsByid(goodsid)
    return redirect("/searchgoods")

@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteuser():
    if request.method == 'GET':

        userid = request.values.get('userid')
        deluserByid(userid)
    return redirect("/searchuser")


@app.route('/deleteproxy', methods=['GET', 'POST'])
def deleteproxy():
    if request.method == 'GET':
        proxyId = request.values.get('proxyid')
        print(proxyId)
        delproxyByid(proxyId)
    return redirect("/")


@app.route('/addgoods', methods=['POST', 'GET'])
def addgoods():
    if request.method == 'GET':
       return render_template('addgoods.html')
    if request.method == 'POST':
        goodsid = request.form['goodsId']
        goodsname = request.form['goodsname']
        goodsimage = request.form['goodsimage']
        goodsCla = request.form['goodsCla']
        goodsPri = request.form['goodsPri']
        CTI = request.form['CTI']
        goodsImAdr = request.form['goodsImAdr']
        addgoods1(goodsid, goodsname, goodsimage, goodsCla, goodsPri, CTI, goodsImAdr)
        info = '商品增加成功'
        return render_template('show.html', info=info)


@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
    if request.method == 'GET':
       return render_template('adduser.html')
    if request.method == 'POST':
        userid = request.form['userid']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        adduser1(userid, username, password, email)
        info = '用户增加成功'
        return render_template('show.html', info=info)


@app.route('/uploadbill', methods=['GET', 'POST'])
def uploadbill():
    form = UploadForm()
    url = None
    if form.validate_on_submit():
        filename = form.upload.data.filename
        url = set_mypic.save(form.upload.data, name='bill.xls')
    return render_template('uploadorder.html', form=form, url=url)




@app.route('/delbillExcel')
def delbillExcel():
    e = delexcel("./upload/bill.xls")
    return render_template('show.html', info=e)



@app.route('/singlegoods')
def singlegoods():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        goods = queryGoodByid(goodsid)
        return render_template('singlegoods.html', goods=goods)


@app.route('/singleproxy')
def singleproxy():
    if request.method == 'GET':
        proxyid = request.values.get('proxyid')
        print(proxyid)
        proxy = queryProxyByid(proxyid)
        if proxy==None:
            return render_template('show.html', info="没有这个代理信息!")
        else:
            a = proxy.proxyId
            print(a)
            n = DBSession.query(User).filter(User.proxyId == a).count()
        return render_template('singleproxy.html', proxy=proxy, VIPNum=n)


@app.route('/showVIP')
def showVIP():
    if request.method == 'GET':
        proxyId = request.values.get('proxyId')
        number = request.values.get('vip')

        user = DBSession.query(User).filter(User.proxyId == proxyId).all()
        if user==None or number < '1':
            return render_template('show.html', info="这个代理没有任何下线")
        else:
            return render_template('showVIP.html', user=user)


@app.route('/showBill/', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/showBill/page/<int:page>')
def showBill(page):
    PER_PAGE=15
    if request.method == 'GET':
        userId = request.values.get('usersid')

        income = DBSession.query(Income).filter(Income.userid == userId).offset(page).limit(PER_PAGE)
        count = DBSession.query(Income).filter(Income.userid == userId).count()
        if income==None:
            return render_template('show.html', info="这个会员没有任何账单")
        else:
            pageination = Pagination(page, PER_PAGE, count)
            return render_template('showBill.html', income=income, pagination=pageination)


@app.route('/showorder', methods=['GET', 'POST'])
def showorder():
    if request.method == 'GET':
        orderNumber = request.values.get('orderNumber')
        print(orderNumber)
        bill = DBSession.query(Bill).filter(Bill.orderNumber == orderNumber).first()
        print(bill.biilID)
        if bill==None:
            return render_template('show.html', info="没有这个账单的任何信息")
        else:
            return render_template('showorder.html', bill=bill)


@app.route('/singleuser')
def singleuser():
    if request.method == 'GET':
        userid = request.values.get('userid')
        user = queryUserByid(userid)
        proxy = DBSession.query(Proxy).filter(Proxy.userid == userid).first()
        if proxy==None:
            return render_template('singleuser.html', user=user)
        else:
            a = proxy.proxyId
            print(a)
            n = queryVIPsbyId(proxy.proxyId).count()

            return render_template('singleuser.html', user=user, VIPNum=n)



@app.route('/editsinglegoods', methods=['GET', 'POST'])
def editsinglegoods():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        goods = queryGoodByid(goodsid)
        return render_template('editsinglegoods.html', goods=goods)
    if request.method == 'POST':

        goodsid = request.form['goodsId']
        goodsname = request.form['goodsname']
        goodsimage = request.form['goodsimage']
        goodsCla = request.form['goodsCla']
        goodsPri =request.form['goodsPri']
        CTI = request.form['CTI']
        goodsImAdr = request.form['goodsImAdr']
        goods = DBSession.query(Goods).filter(Goods.goodsId == goodsid).first()
        if goods:
            goods.goodsName = goodsname
            goods.goodsimage = goodsimage
            goods.goodsCla = goodsCla
            goods.goodPri = goodsPri
            goods.CTI = CTI
            goods.goodsImAdr = goodsImAdr
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)


@app.route('/editsingleBills', methods=['GET', 'POST'])
def editsingleBills():
    if request.method == 'GET':
        goodsid = request.values.get('goodsid')
        bills = DBSession.query(Bill).filter(Bill.goodsid == goodsid).first()

        return render_template('editsingleBills.html', bills=bills)
    if request.method == 'POST':

        biilID = request.form['biilID']
        goodsid = request.form['goodsid']
        Payment = request.form['Payment']
        orderNumber = request.form['orderNumber']
        orderStatus=request.form['orderStatus']

        bills = DBSession.query(Bill).filter(Bill.goodsId == goodsid).first()
        if bills:
            bills.biilID = biilID
            bills.goodsid  = goodsid
            bills.Payment = Payment
            bills.orderNumber = orderNumber
            bills.orderStatus = orderStatus

            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)



@app.route('/editsingleadv', methods=['GET', 'POST'])
def editsingleadv():
    if request.method == 'GET':
        adID = request.values.get('adID')
        print(adID)
        adv1 = DBSession.query(Adv).filter(Adv.adID == adID).first()
        return render_template('editsingleadv.html', adv1=adv1)
    if request.method == 'POST':

        advId = request.form['advId']
        advaddress = request.form['advaddress']
        advlink = request.form['advlink']
        adname = request.form['adname']
        Adv1 = DBSession.query(Adv).filter(Adv.adID == advId).first()
        if Adv1:
            Adv1.adID = advId
            Adv1.advaddress = advaddress
            Adv1.advlink = advlink
            Adv1.adname = adname
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)


@app.route('/editsingleuser', methods=['GET', 'POST'])
def editsingleuser():
    if request.method == 'GET':
        userid = request.values.get('userid')
        user = queryUserByid(userid)
        return render_template('editsingleuser.html', user=user)
    if request.method == 'POST':

        usersid = request.form['usersid']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        integration =request.form['integration']
        proxyId = request.form['proxyId']
        user = DBSession.query(User).filter(User.userid == usersid).first()
        if user:
            user.usersid = usersid
            user.username = username
            user.password = password
            user.email = email
            user.integration = integration
            user.proxyId = proxyId
            DBSession.commit()
            info = '插入成功'
            return render_template('show.html', info=info)


@app.route('/searchorder/', defaults={'page': 0}, methods=['GET', 'POST'])
@app.route('/searchorder/page/<int:page>')
def searchorder(page):
    PER_PAGE=15
    if request.method == 'GET':
        Bills = DBSession.query(Bill).offset(page).limit(PER_PAGE)
        count = DBSession.query(Bill).count()
        if not Bills and page != 1:
            abort(404)
    pageination = Pagination(page, PER_PAGE, count)
    return render_template('searchorder.html', Bills=Bills, pagination=pageination)


@app.route('/searchbillbyID', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/searchbillbyID/page/<int:page>')
def searchbillbyID(page):
    PER_PAGE=15
    if request.method == 'POST':
        bill = request.form['searchID']
        bill1 = DBSession.query(Bill).filter(Bill.orderNumber == bill).offset(page).limit(PER_PAGE)
        count = DBSession.query(Bill).filter(Bill.orderNumber == bill).count()
        if not bill and page != 1:
            abort(404)
        pageination = Pagination(page, PER_PAGE, count)

        return render_template('searchorder1.html', bill=bill1, pagination=pageination)
    else:
        erro = "没有找到商品,,请正确输入订单编号!"

        return render_template('show.html', info=erro)



@app.route('/addorder')
def addorder():
    return render_template('addorder.html')





@app.route('/Homedaily', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/Homedaily/page/<int:page>')
def Homedaily(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家日用%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家日用%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%美食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count, count2=count2,count4=count4,count5=count5,
                           count6=count6, count7=count7,count8=count8,count9=count9,Claname='居家日用')


@app.route('/shoes', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/shoes/page/<int:page>')
def shoes(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()
        count3 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%母婴%')).count()
        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%鞋包配饰%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%美食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%文体车品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count3=count3,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9, Claname='女鞋')


@app.route('/book', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/book/page/<int:page>')
def book(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='汽车用品')


@app.route('/jiu', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/jiu/page/<int:page>')
def jiu(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodPri <=10).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodPri <=10).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='九元包邮')


@app.route('/charts', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/charts/page/<int:page>')
def charts(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='抢卷排行')

@app.route('/juanlive', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/juanlive/page/<int:page>')
def juanlive(page):
    PER_PAGE = 32
    if request.method == 'GET':
        goods = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.couponCount.desc()).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.couponCount.desc()).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        if not goods and page != 1:
            render_template('fshow.html', info="找不到这个网页")
    pageination = Pagination(page, PER_PAGE, count)
    if session.get('username')== None:
        return render_template('index.html', goods=goods, pagination=pageination)
    return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2,count4=count4,count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9,Claname='抢卷直播')


@app.route('/searchmore', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/searchmore/page/<int:page>')
def searchmore(page):
    PER_PAGE = 32
    if request.method == 'POST':
        goodsname = request.form['goodsname']
        word=["%"+goodsname+"%"]
        goods = DBSession.query(Goods).filter(and_(Goods.goodsName.like(word), Goods.CTI >= 20)).offset(page).limit(PER_PAGE)
        count = DBSession.query(Goods).filter(and_(Goods.goodsName.like(word), Goods.CTI >= 20)).count()
        count2 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%服装%')).count()

        count4 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%化妆品%')).count()
        count5 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%居家%')).count()
        count6 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%女鞋%')).count()
        count7 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%零食%')).count()
        count8 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%汽车用品%')).count()
        count9 = DBSession.query(Goods).filter(Goods.CTI >= 20).filter(Goods.goodsCla.like('%数码家电%')).count()
        pageination = Pagination(page, PER_PAGE, count)
        return render_template('showgoods.html', username=session.get('username'), goods=goods, pagination=pageination,
                           count1=count,count2=count2, count4=count4, count5=count5,
                           count6=count6,count7=count7,count8=count8,count9=count9, Claname=goodsname)


@app.route('/login', methods=['GET', 'POST'])
def login():
    page = 1
    PER_PAGE = 16
    if request.method == 'get':
        return redirect('/')
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        print('执行到此01')
        username = session.get('username')
        print('执行到此02')
        password = session.get('password')
    if username and password:
            if queryUserByname(username) != None:
              if DBSession.query(User).filter(User.username == username and User.password == password):
                username = session.get('username')
                userid = queryUserByname(username).userid
                goods1 = DBSession.query(Goods).filter(Goods.CTI >= 20).offset(page).limit(PER_PAGE)
                goods2 = DBSession.query(Goods).filter(Goods.CTI >= 20).order_by(Goods.shopCount.desc()).offset(page).limit(
                PER_PAGE)
                count = DBSession.query(Goods).filter(Goods.CTI >= 20).count()
                pageination = Pagination(page, PER_PAGE, count)
                session['userid'] = userid
                return render_template('index.html', username=username, goods=goods1, goods2=goods2,
                                       pagination=pageination)
                if not goods1 and page != 1:
                    render_template('fshow.html', info="找不到这个网页")
              else:
                  return redirect('/')

            else:
                return redirect('/')



@app.route('/unregister')
def unregister():

    return render_template('index.html')

@app.route('/xu6735625')
def xu6735625():
    n = count()
    g = countG()
    o = countO()
    P = queryAll(Proxy)

    return render_template('test.html', countuser=n, countgoods=g, countorder=o, proxy=P)



def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['email'] = request.form['email']

        username = session.get('username')
        password = session.get('password')
        email = session.get('email')
        if username == ''or password == '':
            return "<script>alert('请输入用户名')</script>" and redirect('/')
        else:
            adduser1(username, password, email)
    if username == queryUserByname(username).username and password == queryUserByname(username).password:
        # queryUserByname(username) != None:
        return "注册成功" and redirect('/')
    else:
        return render_template('index.html')


@app.route('/500')
def error():
    return render_template('500.html')


@app.route('/404')
def error404():
    return render_template('404.html')


@app.route('/Billsubmit', methods=['POST', 'GET'])
def Billsubmit():
    if request.method == 'POST':
        Billnumber = request.form['bill']
        username = session.get('username')
        userid = queryUserByname(username).userid
        print(Billnumber)
        print(username)
        print(userid)
        if DBSession.query(Bill).filter(Bill.orderStatus=='订单结账'):
            if queryBillbynumber(Billnumber)!=None and queryincomeByNumber(Billnumber)==None:
                intergration = queryBillbynumber(Billnumber).payment * 10
                addIntegration(userid, Billnumber)
                addincome(userid, Billnumber, username)
                return render_template('fshow.html', info='你已经成功入库订单,并且拿到了积分')
            elif queryBillbynumber(Billnumber)==None:
                return render_template('fshow.html', info='没有这个订单')
            elif queryincomeByNumber(Billnumber)!=None:
                return render_template('fshow.html', info='这个订单已经入库了!!')
            else:
                return render_template('selfinfo.html', info='没有成功拿到积分')
        else:
            return render_template('fshow.html', info='没有结账的订单不能入库!')
    if request.method == 'get':
        userid = session.get('userid')
        return render_template('/selfinfo.html', userid=userid)

@app.route('/selfinfo')
def selfinfo():
    if session.get('username') == None or session.get('username') == "":
        return redirect('/')
    else:
        username = session.get('username')
        user = queryUserByname(username)

        return render_template('selfinfo.html', user=user, userid=user.userid)


@app.route('/adinfo')
def adinfo():
    if session.get('username') == None or session.get('username') == "":
        return redirect('/')
    else:
        username = session.get('username')
        user = queryUserByname(username)
        return render_template('adinfo.html', user=user, userid=user.userid)


@app.route('/updeteUserinfo', methods=['GET', 'POST'])
def updeteUserinfo():
    if request.method == 'GET':
        if request.values.get('id') == None or request.values.get('id') == "":
            return redirect('/')
        else:
            userid = request.values.get('id')

            user = queryUserByid(userid).first()

        return render_template('updeteUserinfo.html', user=user, userid=userid)
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        proxyId = request.form['proxyId']
        integration = request.form['integration']

        users = DBSession.query(User).filter(User.username == username).first()
        if users!=None:
            users.username = username
            users.password = password
            users.email = email
            users.proxyId = proxyId
            users.integration = integration
            DBSession.commit()
            info = '用户增加成功'
            return render_template('fshow.html', info=info)
        else:
            return render_template('fshow.html', info="没有查询到任何用户")


@app.route('/adproxy', methods=['GET', 'POST'])
def adproxy():
    if request.method == 'GET':
        username = session.get('username')
        a = DBSession.query(Proxy).filter(Proxy.username == username).all()
        if username == None:
            return render_template('fshow.html', info='请登录之后再来这个模块')
        elif a:
            userid = request.values.get('userid')
            p = DBSession.query(Proxy).filter(Proxy.userid == userid).first()
            countB = DBSession.query(User).filter(User.proxyId == p.proxyId).count()
            countP = DBSession.query(User.userid).filter(User.proxyId == p.proxyId).count()
            return render_template('adproxy.html', countB=countB, countP=countP)
        else:
            return render_template('fshow.html', info='你还不是代理不能进入这个模块')




@app.route('/applyproxy', methods=['GET', 'POST'])
def applyproxy():
    if request.method == 'GET':
        return render_template('applyproxy.html')
    if request.method == 'POST':
        username = request.form.get('username')
        userid = session.get('userid')
        email = request.form.get('email')
        telephone = request.form.get('telephone')

        addadv(userid, username, email, telephone)
        return render_template('fshow.html', info="申请成功!请等待管理员回复")


if __name__ == '__main__':
    app.run(debug=True)
