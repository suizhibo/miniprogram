from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now())


# 使用用户表
class User(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'User'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(15), nullable=False)
    nick_name = db.Column(db.String(15), nullable=False)
    school = db.Column(db.String(15))
    college = db.Column(db.String(15))
    created_at = db.Column('createdAt', db.TIMESTAMP, default=datetime.now())

    orders = db.relationship('Order', backref='user', lazy='dynamic')
    addresses = db.relationship('Address', backref='user', lazy='dynamic')

class Order(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Order'

    # 设定结构体对应表格的字段
    id = db.Column(db.String(15), primary_key=True)
    status = db.Column(db.String(15), nullable=False)
    user_name = db.Column(db.String(15), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    kg = db.Column(db.String(15))
    money = db.Column(db.String(15))
    date_time = db.Column('dataTime', db.TIMESTAMP,
                           default=datetime.now())
    created_at = db.Column('createdAt', db.TIMESTAMP,
                           default=datetime.now())

    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'))
    address_id = db.Column(db.Integer(), db.ForeignKey('Address.id'))


class Address(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Address'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(15), nullable=False)
    user_name = db.Column(db.String(15), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    detailed_address = db.Column(db.String(15), nullable=False)
    created_at = db.Column('createdAt', db.TIMESTAMP,
                           default=datetime.now())

    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'))
