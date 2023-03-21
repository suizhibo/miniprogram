import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'root')
db_address = os.environ.get("MYSQL_ADDRESS", '127.0.0.1:3306')

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

#weixin
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
get_phone_number_url = "https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token="

