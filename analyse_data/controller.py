# encoding: utf-8
__author__ = 'fengshenjie'
from analyse_data.models import *
import json, traceback


# 返回tb_apps中所有数据
def db_get_tb_apps():
    try:
        apps = Apps.query.all()
        return apps
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_apps')
        print(e)
        return []


# 根据包名，以json格式返回app表中单条数据的完整信息
# {
#     "id": 11,
#     "name": "中邮钱包",
#     "developer": "中邮消费金融有限公司",
#     "description": "没什么好描述的",
#     "package": "com.youcash"
# }
def db_get_appinformation_by_package(package):
    try:
        app = Apps.query.filter(Apps.package == package).first()
        return app
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_apps')
        print(e)
        return None


# 根据package查询对应app_id
def get_id_by_package(package):
    try:
        app_id = Apps.query.filter(Apps.package == package).first().id
        return app_id
    except Exception as e:
        print('The Package does not exit!')
        print(e)
        return -1

# 根据package查询对应appname
def get_appname_by_pkgname(pkgname):
    try:
        name=Apps.query.filter(Apps.package==pkgname).first().name
        return name
    except Exception as e:
        traceback.print_exc()
        return ''


# 根据package，返回日下载量记录中某app的所有记录
def db_get_daydownloads(package):
    app_id = get_id_by_package(package)
    try:
        records_all = RecordsDay.query.filter(RecordsDay.app_id == app_id)
        return records_all
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_records_day')
        print(e)
        return []


# 根据package，day_counter返回若干天内日下载量记录中某app的所有记录
def db_get_daydownloads_by_day(package, day_counter):
    import datetime
    from sqlalchemy import and_
    app_id = get_id_by_package(package)
    try:
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # 最早的一天
        early_day = (datetime.datetime.now() - datetime.timedelta(days=day_counter)).strftime("%Y-%m-%d")
        records = RecordsDay.query.filter(
            and_(RecordsDay.app_id == app_id, RecordsDay.date >= early_day, RecordsDay.date <= yesterday)
            ).all()
        return records
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_records_day')
        print(e)
        return []

def db_get_totaldownloads(pkgname):
    app_id = get_id_by_package(pkgname)
    try:
        records = RecordsDetail.query.filter(
            RecordsDetail.app_id == app_id).order_by(
            db.desc(RecordsDetail.tick)).all()
        return records
    except Exception as e:
        traceback.print_exc()
        return []

# 根据package，返回tb_version_history中该app的所有记录
def db_get_versions(package):
    app_id = get_id_by_package(package)
    try:
        versions = Version.query.filter(Version.app_id == app_id).all()
        return versions
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_version_history')
        print(e)
        return []


# 获取tb_comments中某app若干天前在某个应用市场上的评论信息
def db_get_comments(package, market, early_day, yesterday):
    app_id = get_id_by_package(package)
    try:
        from sqlalchemy import and_
        comments = Comment.query.filter(
            and_(Comment.app_id == app_id, Comment.market == market, Comment.date >= early_day,
                 Comment.date <= yesterday)
            ).all()
        return comments
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_comment')
        print(e)
        return []

# 对tb_apps表的name进行模糊匹配，返回对应app信息
def db_get_apps_by_name(name):
    try:
        apps = Apps.query.filter(Apps.name.like("%" + name + "%")).all()
        return apps
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_apps')
        print(e)
        return []

if __name__ == '__main__':
    pass
