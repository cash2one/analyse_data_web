SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/analyse_data?charset=utf8'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rrrrrr@localhost:3306/analyse_data_test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
FSJ = 'fsj'
# SECRET_KEY = 'hard to guess' # 通用秘钥，在flask以及包括wtf的多个第三方扩展使用。
# WTF_CSRF_SECRET_KEY = 'a random string' # 为wtf配置独有的秘钥