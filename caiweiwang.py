from flask import Flask, render_template, redirect, url_for, session, request,abort

from model.user import queryUserByname, adduser1, count, User, queryAll, queryUserByid,deluserByid


from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES,configure_uploads
from model.adv import Adv, queryAll
from model.tools import Base,engine

from controller.home.home import home
from controller.home.searchGoods import search
from controller.home.homeNav import homeNav
from controller.home.homeBill import homeBill
from controller.home.homeError import homeError
from controller.home.homeProxy import homeProxy
from controller.home.homeOrder import homeOrder
from controller.home.homeUser import homeUser
from controller.admin.advertisementView import advadmin
from controller.admin.auditAdmin import adminAudit
from controller.admin.billAdmin import billadmin
from controller.admin.orderAdmin import orderAdmin
from controller.admin.goodsAdmin import goodsadmin
from controller.admin.proxyAdmin import adminProxy
from controller.admin.userView import useradmin
from controller.admin.indexAdmin import indexadmin

Base.metadata.create_all(engine)
app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'  # session会话必备
app.register_blueprint(blueprint=home, url_prefix='/')
app.register_blueprint(blueprint=search, url_prefix='/')
app.register_blueprint(blueprint=homeNav, url_prefix='/')
app.register_blueprint(blueprint=homeBill, url_prefix='/')
app.register_blueprint(blueprint=homeError, url_prefix='/')
app.register_blueprint(blueprint=homeProxy, url_prefix='/')
app.register_blueprint(blueprint=homeUser, url_prefix='/')

app.register_blueprint(blueprint=orderAdmin, url_prefix='/admin')
app.register_blueprint(blueprint=advadmin, url_prefix='/admin')
app.register_blueprint(blueprint=adminAudit, url_prefix='/admin')
app.register_blueprint(blueprint=billadmin, url_prefix='/admin')
app.register_blueprint(blueprint=goodsadmin, url_prefix='/admin')
app.register_blueprint(blueprint=adminProxy, url_prefix='/admin')
app.register_blueprint(blueprint=useradmin, url_prefix='/admin')
app.register_blueprint(blueprint=indexadmin, url_prefix='/admin')

set_mypic = UploadSet('mypic')
bootstrap = Bootstrap(app)
app.config['UPLOADED_MYPIC_DEST'] = './upload'
app.config['UPLOADED_MYPIC_ALLOW'] = IMAGES
configure_uploads(app, set_mypic)
app.config['SECRET_KEY'] = 'xxxxx'


@app.errorhandler(401)
def page_unauthorized(error):
    return render_template('error.html', info="401")


@app.errorhandler(404)
def page_unauthorized(error):
    return render_template('error.html', info="404")


@app.errorhandler(403)
def page_unauthorized(error):
    return render_template('error.html', info="403")


@app.errorhandler(500)
def page_unauthorized(error):
    return render_template('error.html', info="500")


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


app.jinja_env.globals['url_for_other_page'] = url_for_other_page


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
