# encoding: utf-8
__author__ = 'fengshenjie'
from flask import render_template
import json
from flask import request, Response, make_response
from analyse_data import app
from analyse_data.controller import *

header = {'Content-type': 'application/json;charset=utf-8'}


@app.route('/product_cmp/<string:a>/<string:b>/')
def product_cmp_ab(a, b):
    data = {'a': a,
            'b': b
            }
    return json.dumps(data), 200, header


@app.route('/product_cmp/<string:a>/')
def product_cmp_testone(a):
    d = {}
    return json.dumps(d)


# 以json形式返回整个tb_apps表
# by zhengzhirui

@app.route('/api_1_0/allapps/')
def get_all_apps():
    apps = db_get_tb_apps()
    if apps == None:
        return json.dumps({}), 200, header
    apps_array = []
    app_counter = 0
    for app in apps:
        apps_array.append(app.get_dict())
    return json.dumps(apps_array), 200, header


# 根据包名，以json格式返回app表中单条数据的完整信息
# {
#     "id": 11,
#     "name": "中邮钱包",
#     "developer": "中邮消费金融有限公司",
#     "description": "没什么好描述的",
#     "package": "com.youcash"
# }

@app.route('/api_1_0/appinformation/<package>/')
def get_appinformation_by_package(package):
    app = db_get_appinformation_by_package(package)
    if app == None:
        return json.dumps({}), 200, header
    return json.dumps(app.get_dict()), 200, header


# 根据package，以json格式返回app在各应用市场的下载量
@app.route('/api_1_0/downloads_in_markets/<package>/')
def get_appdownloads_in_markets(package):
    records_all = db_get_daydownloads(package)
    if records_all == None:
        return json.dumps({}), 200, header
    # 计算在各应用市场的总下载量
    # eg. downloads_in_markets['应用宝']=2000
    downloads_in_markets = {}
    for record_all in records_all:
        try:
            downloads_in_markets[record_all.market] += record_all.downloads_day
        except:
            downloads_in_markets[record_all.market] = record_all.downloads_day

    return json.dumps(downloads_in_markets), 200, header


# 根据package，以json格式返回app在<day_counter>天前一直到昨天，每一天的下载量
# {
#     "2017-08-22": 80,
#     "2017-08-21": 70,
#     "2017-08-20": 90,
#     "2017-08-19": 90,
#     "2017-08-18": 90,
#     "2017-08-17": 90,
#     "2017-08-16": 90
# }
@app.route('/api_1_0/downloads/<package>/<int:day_counter>/')
def get_appdownloads_on_days(package, day_counter=7):
    import datetime
    records_daily = db_get_daydownloads_by_day(package, day_counter)
    downloads_on_days = {}
    for i in range(day_counter):
        the_day = (datetime.datetime.now() - datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
        downloads_on_days[the_day] = 0
    for record in records_daily:
        try:
            downloads_on_days[str(record.date)[:10]] += record.downloads_day
        except:
            pass

    return json.dumps(downloads_on_days), 200, header


# 根据package查找某app的版本历史信息
# {
#     "0": {
#         "id": 1,
#         "app_id": 14,
#         "name": "0.9",
#         "update_time": "2017-08-23 00:00:00",
#         "update_description": "xxx"
#     },
#     "1": {
#         "id": 2,
#         "app_id": 14,
#         "name": "0.9",
#         "update_time": "2017-08-22 00:00:00",
#         "update_description": "xxx"
#     }
# }
@app.route('/api_1_0/versionhistory/<package>/')
def get_versionhistory(package):
    versions = db_get_versions(package)
    if versions == None:
        return json.dumps({}), 200, header
    versions_array = []
    for version in versions:
        versions_array.append(version.get_dict())
    # 将日期转化为字符串供json处理
    for version in versions_array:
        version['update_time'] = version['update_time'].strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps(versions_array), 200, header


# 根据package获取某app在某段时间内在某个应用市场的好坏评数量
# {
#     "2017-08-23": {
#         "positive": 1,
#         "negative": 2
#     },
#     "2017-08-22": {
#         "positive": 0,
#         "negative": 0
#     },
#     "2017-08-21": {
#         "positive": 0,
#         "negative": 1
#     }
# }
@app.route('/api_1_0/scorehistory/package=<package>/market=<market>/duration=<duration>')
def get_scorehistory(package, market, duration):
    import datetime
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    day_counter = 7
    if duration == '7_day':
        day_counter = 7
    elif duration == '1_month':
        day_counter = 30
    else:
        pass
    # 最早的一天
    early_day = (datetime.datetime.now() - datetime.timedelta(days=day_counter)).strftime("%Y-%m-%d")

    # 根据package，market，日期查询对应评论
    comments = db_get_comments(package, market, early_day, yesterday)
    if comments == None:
        return json.dumps({}), 200, header

    # 要返回json的array格式
    dict_of_comment_positive_negative = {}
    today = datetime.datetime.now()
    # 初始化dict
    for i in range(day_counter):
        dateString = (today - datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
        dict_of_comment_positive_negative[dateString] = {'positive': 0, 'negative': 0}

    for comment in comments:
        # 评论分数3或3以上为好评
        if comment.score >= 3:
            dict_of_comment_positive_negative[comment.date.strftime("%Y-%m-%d")]['positive'] += 1
        else:
            dict_of_comment_positive_negative[comment.date.strftime("%Y-%m-%d")]['negative'] += 1

    return json.dumps(dict_of_comment_positive_negative), 200, header


@app.route('/api_1_0/searchapps/<appname>')
def search_apps(appname):
    apps = db_get_apps_by_name(appname)
    apps_array = []
    for app in apps:
        apps_array.append(app.get_dict())
    return json.dumps(apps_array), 200, header


# 模糊匹配appname，返回appid，appname，总下载量
@app.route('/api_1_0/searchapps2/<appname>')
def search_apps2(appname):
    apps = db_get_apps_by_name(appname)
    result_list = []
    for app in apps:
        record = db_get_newest_downloads(app.id)

        if record is None:
            result_list.append({"app_id": app.id, "app_name": app.name, "downloads_total": '无数据'})
        else:
            result_list.append({"app_id": app.id, "app_name": app.name, "downloads_total": record.downloads_total})
    return json.dumps(result_list), 200, header
