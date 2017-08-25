# encoding: utf-8
__author__ = 'fengshenjie'
from analyse_data.models import *
import json


# 返回tb_apps中所有数据
def DB_get_tb_apps():
    try:
        apps = Apps.query.all()
        return apps
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_apps')
        print(e)


# 根据包名，以json格式返回app表中单条数据的完整信息
# {
#     "id": 11,
#     "name": "中邮钱包",
#     "developer": "中邮消费金融有限公司",
#     "description": "没什么好描述的",
#     "package": "com.youcash"
# }
def DB_get_AppInformation_by_Package(package):
    try:
        app = Apps.query.filter(Apps.package == package).first()
        return app
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_apps')
        print(e)
        pass


# 根据package查询对应app_id
def get_id_by_package(package):
    try:
        app_id = Apps.query.filter(Apps.package == package).first().id
        return app_id
    except Exception as e:
        print('The Package does not exit!')
        print(e)


# 根据package，返回日下载量记录中某app的所有记录
def DB_get_DayDownloads(package):
    app_id = get_id_by_package(package)
    try:
        records_all = RecordsDay.query.filter(RecordsDay.app_id == app_id)
        return records_all
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_records_day')
        print(e)
        pass


# 根据package，返回tb_version_history中该app的所有记录
def DB_get_Versions(package):
    app_id = get_id_by_package(package)
    try:
        versions = Version.query.filter(Version.app_id == app_id)
        return versions
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_version_history')
        print(e)
        pass


# 获取tb_comments中某app若干天前在某个应用市场上的评论信息
def DB_get_comments(package, market, early_day, yesterday):
    app_id = get_id_by_package(package)
    try:
        from sqlalchemy import and_
        comments = Comment.query.filter(
            and_(Comment.app_id == app_id, Comment.market == market, Comment.date >= early_day,
                 Comment.date <= yesterday))
        return comments
    except Exception as e:
        print('::QueryFailure::\n'
              '::Information:tb_comment')
        print(e)
        pass


if __name__ == '__main__':
    pass
