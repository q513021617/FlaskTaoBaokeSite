from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from .tools import Base, DBSession, engine


class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    password = Column(String(128), unique=True, index=True)
    email = Column(String(64), unique=True, index=True)

    def __str__(self):
        return self

    def __int__(self, username, password, email):
        return


def deluserByid(userid):
    user = DBSession.query(User).filter(User.userid == userid).one()
    DBSession.delete(user)
    DBSession.commit()


def queryUserByid(userid):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(User).filter(User.userid == userid).one()
    # 关闭Session:
    return user


def queryUserByname(username):

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = DBSession.query(User).filter(User.username == username).one()
    # 关闭Session:
    return user


def adduser(username, password, email):
    # 创建新User对象:
    new_user = User(username=username, password=password, email=email)
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
    score = DBSession.query(userid)
    return score
