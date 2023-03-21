import requests

from datetime import datetime
from flask import render_template, request

import config
from run import app
from wxcloudrun.dao import *
from wxcloudrun.model import Counters, User, Order, Address
from wxcloudrun.response import make_succ_empty_response, make_succ_response, \
    make_err_response


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route("/api/checkRegist", methods=['post'])
def check_regist():
    openid = request.headers['X-WX-OPENID']
    return make_succ_response(openid)
    # user = User.query.filter(User.openid == openid).first()
    # return make_succ_response(1) if user is None else make_succ_response(0)


@app.route("/api/addUser", methods=['post'])
def add_user():
    """
       :return:添加信息成功
       """

    # 获取请求体参数
    params = request.get_json()
    user = User()
    user.openid = params['openid']
    user.nick_name = "low"
    user.name = params['name']
    user.school = params['school']
    user.college = params['college']
    user.created_at = datetime.now()
    try:
        insert_user(user)
        return make_succ_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response("添加用户失败")


@app.route("/api/getUser")
def get_user():
    """
        :return:计数结果/清除结果
        """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    if action == "all":
        try:
            return make_succ_response(query_alluser(params['page']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)

    if action == "id":
        try:
            return make_succ_response(query_userbyid(params['id']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)


@app.route("/api/updateUser")
def update_user():
    """
    :return:void
    """

    # 获取请求体参数
    params = request.get_json()
    id = params['id']
    user = query_userbyid(id)
    user.nick_name = params['nick_name']
    user.name = params['name']
    user.school = params['school']
    user.college = params['college']
    try:
        update_userbyid(user)
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response(ex)


@app.route("/api/addOrder", methods=['post'])
def add_order():
    """
       :return:添加信息成功
       """

    # 获取请求体参数
    params = request.get_json()
    order = Order()
    order.user_id = params['user_id']
    order.user_name = params['user_name']
    order.address_id = params['address_id']
    order.phone_number = params['phone_number']
    order.date_time = params['date_time']
    try:
        insert_order(order)
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response("添加订单失败")


@app.route("/api/getOrder")
def get_order():
    """
        :return:订单
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    if action == "all":
        try:
            return make_succ_response(query_allorder(params["page"]))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)

    if action == "userid":
        try:
            if params['status'] is None:
                return make_succ_response(query_orderbyuserid(params['userid'],
                                                          params['page']))
            return make_succ_response(query_orderbyuseridandstatus(
                params['userid'], params['status'], params['page']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)

    if action == "id":
        try:
            return make_succ_response(query_orderbyid(params['id']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)


@app.route("/api/updateOrder")
def update_order():
    """
    :return:void
    """

    # 获取请求体参数
    params = request.get_json()
    id = params['id']
    order = query_orderbyid(id)
    order.phone_number = params['phone_number']
    order.user_name = params['user_name']
    order.kg = params['kg']
    order.money = params['money']
    order.status = params['status']
    try:
        update_orderbyid(order)
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response(ex)


@app.route("/api/deleteOrder")
def delete_order():
    """
    :return:void
    """

    # 获取请求体参数
    params = request.get_json()
    try:
        delete_order(params['id'])
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response(ex)


@app.route("/api/addAddress", methods=['post'])
def add_address():
    """
       :return:添加信息成功
       """

    # 获取请求体参数
    params = request.get_json()
    address = Address()
    address.user_id = params['user_id']
    address.detailed_address = params['detailed_address']
    address.city = params['city']
    try:
        insert_address(address)
        return make_succ_empty_response()
    except Exception as ex:
        return make_err_response("添加地址失败")


@app.route("/api/getAddress")
def get_address():
    """
        :return:地址
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    if action == "userid":
        try:
            return make_succ_response(query_alladdressbyuserid(
                params['userid'], params['page']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)

    if action == "id":
        try:
            return make_succ_response(query_addressbyid(params['id']))
        except Exception as ex:
            logging.info(ex)
            return make_err_response(ex)


@app.route("/api/updateAddress")
def update_address():
    """
    :return:void
    """

    # 获取请求体参数
    params = request.get_json()
    id = params['id']
    address = query_addressbyid(id)
    address.phone_number = params['phone_number']
    address.user_name = params['user_name']
    address.city = params['city']
    address.detailed_address = params['detailed_address']
    try:
        update_addressbyid(address)
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response(ex)


@app.route("/api/deleteAddress")
def delete_address():
    """
    :return:void
    """

    # 获取请求体参数
    params = request.get_json()
    try:
        delete_addressbyid(params['id'])
        return make_succ_empty_response()
    except Exception as ex:
        logging.info(ex)
        return make_err_response(ex)



@app.route("/api/getUserPhone")
def get_user_phone():
    try:
        # 获取请求体参数
        params = request.get_json()
        data = {
            "code": params['code']
        }
        url = config.get_phone_number_url.format(config.ACCESS_TOKEN)
        respond = requests.post("url", json=data)
        if respond.status_code == 200:
            respond_data = respond.json()
            phone_number = respond_data['phone_info']['phoneNumber']
            result = {"phoneNumber": phone_number}
            return make_succ_response(result)
    except Exception as ex:
        logging.info("获取用户手机号失败{}".format(ex))
    return make_err_response("获取用户手机号失败")