import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Counters, User, Order, Address

# 初始化日志
logger = logging.getLogger('log')


def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        counter = query_counterbyid(counter.id)
        if counter is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_counterbyid errorMsg= {} ".format(e))


def insert_user(user):
    """
    User
    :param user: User
    """
    try:
        db.session.add(user)
        db.session.commit()
    except OperationalError as e:
        raise Exception("insert_user errorMsg= {} ".format(e))


def query_alluser(page=None):
    """
    查询所有User实体
    :return: User实体列表
    """
    try:
        if page is None:  # 如果没有page则显示第一页
            page = 1
        page_data = User.query.order_by(
            User.id.asc()
        ).paginate(page=page, per_page=10)
        return page_data
    except OperationalError as e:
        raise Exception("query_alluser errorMsg= {} ".format(e))


def query_userbyid(id):
    """
    根据ID查询User实体
    :param id: User的ID
    :return: User实体
    """
    try:
        return User.query.filter(User.id == id).first()
    except OperationalError as e:
        raise Exception("query_orderbyid errorMsg= {} ".format(e))


def update_userbyid(user):
    """
    根据ID更新user的值
    :param user实体
    """
    try:
        user = query_userbyid(user.id)
        if user is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        raise Exception("update_userbyid errorMsg= {} ".format(e))


def insert_order(order):
    """
    Order
    :param order: Order
    """
    try:
        db.session.add(order)
        db.session.commit()
    except OperationalError as e:
        raise Exception("insert_order errorMsg= {} ".format(e))


def query_allorder(page=None):
    """
    查询所有Order实体
    :param:page 当前页号
    :return: Order实体列表
    """
    try:
        if page is None:  # 如果没有page则显示第一页
            page = 1
        page_data = Order.query.order_by(
            Order.id.asc()
        ).paginate(page=page, per_page=10)
        return page_data
    except OperationalError as e:
        raise Exception("query_allorder errorMsg= {} ".format(e))


def query_orderbyid(id):
    """
    根据ID查询order实体
    :param id: Order的ID
    :return: Order实体
    """
    try:
        return Order.query.filter(Order.id == id).first()
    except OperationalError as e:
        raise Exception("query_orderbyid errorMsg= {} ".format(e))


def query_orderbyuserid(userid, page=None):
    """
    根据userID查询order实体
    :param userid: user的ID
    :param page: 页号
    :return: Order实体列表
    """
    try:
        if page is None:  # 如果没有page则显示第一页
            page = 1
        page_data = Order.query.filter(User.id == userid).order_by(
            Order.id.asc()
        ).paginate(page=page, per_page=10)
        return page_data
    except OperationalError as e:
        raise Exception("query_orderbyuserid errorMsg= {} ".format(e))


def query_orderbyuseridandstatus(userid, status, page=None):
    """
    根据userID查询order实体
    :param userid: user的ID
    :param status: 订单状态
    :param page: 页号
    :return: Order实体列表
    """
    try:
        if page is None:  # 如果没有page则显示第一页
            page = 1
        page_data = Order.query.filter(User.id == userid,
                                       Order.status == status).order_by(
            Order.id.asc()
        ).paginate(page=page, per_page=10)
        return page_data
    except OperationalError as e:
        raise Exception("query_orderbyuserid errorMsg= {} ".format(e))


def update_orderbyid(order):
    """
    根据ID更新order的值
    :param Order实体
    """
    try:
        order = query_orderbyid(order.id)
        if order is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        raise Exception("update_orderbyid errorMsg= {} ".format(e))


def delete_orderbyid(id):
    """
        根据ID删除order
        :param id
        """
    try:

        Order.query.filter(Order.id == id).delete()
        db.session.commit()
    except OperationalError as e:
        raise Exception("detele_orderbyid errorMsg= {} ".format(e))


def insert_address(address):
    """
    Order
    :param address: Address
    """
    try:
        db.session.add(address)
        db.session.commit()
    except OperationalError as e:
        raise Exception("insert_address errorMsg= {} ".format(e))


def query_alladdressbyuserid(userid, page=None):
    """
    查询所有Address实体
    :param:userid 用户id
    :param:page 当前页号
    :return: Address实体列表
    """
    try:
        if page is None:  # 如果没有page则显示第一页
            page = 1
        page_data = Address.query.filter(Address.user_id == userid).order_by(
            Address.id.asc()
        ).paginate(page=page, per_page=10)
        return page_data
    except OperationalError as e:
        raise Exception("query_alladdressbyuserid errorMsg= {} ".format(e))


def query_addressbyid(id):
    """
    根据ID查询address实体
    :param id: address的ID
    :return: Address实体
    """
    try:
        return Address.query.filter(Address.id == id).first()
    except OperationalError as e:
        raise Exception("query_addressbyid errorMsg= {} ".format(e))


def update_addressbyid(address):
    """
    根据ID更新address的值
    :param Address实体
    """
    try:
        address = query_addressbyid(Address.id)
        if address is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        raise Exception("update_addressbyid errorMsg= {} ".format(e))


def delete_addressbyid(id):
    """
        根据ID删除address
        :param id
        """
    try:

        Address.query.filter(Address.id == id).delete()
        db.session.commit()
    except OperationalError as e:
        raise Exception("detele_addressbyid errorMsg= {} ".format(e))