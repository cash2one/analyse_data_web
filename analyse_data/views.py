from flask import render_template
import json
from flask import request
from analyse_data import app
from analyse_data.controller import *


@app.route('/hello/')
def hello_world():
    url = request.args
    return render_template('hello.html')


@app.route('/')
def index():
    apps = db_get_tb_apps()
    return render_template('index.html', apps=apps)


@app.route('/product_cmp/')
def product_cmp():
    return render_template('product_cmp.html')


@app.route('/user/<name>')
def user(name):
    return render_template('base.html', name=name)


@app.route('/downloads/total/<pkgname>/')
def totaldownloads(pkgname):
    # 总下载数据
    records_all = db_get_daydownloads(pkgname)
    downloads_in_markets = {}
    for record_all in records_all:
        try:
            downloads_in_markets[record_all.market] += record_all.downloads_day
        except:
            downloads_in_markets[record_all.market] = record_all.downloads_day

    # 最近若干天下载量，默认7天
    import datetime
    day_counter = 30
    records_daily = db_get_daydownloads_by_day(pkgname, day_counter)
    downloads_on_days = {}
    for i in range(day_counter):
        the_day = (datetime.datetime.now() - datetime.timedelta(days=i + 1)).strftime("%Y-%m-%d")
        downloads_on_days[the_day] = 0
    for record in records_daily:
        try:
            downloads_on_days[str(record.date)[:10]] += record.downloads_day
        except:
            pass
    return render_template('totaldownloads.html', downloads_in_markets=downloads_in_markets,
                           downloads_on_days=downloads_on_days)


@app.route('/downloads/daily/')
def dailydownloads():
    pass


@app.route('/comments/')
def comments():
    pass


@app.route('/monitoring/')
def monitoring():
    pass


@app.route('/keywords/<pkgname>/')
def keywords(pkgname):
    return render_template('keywords.html', pkgname=pkgname)


@app.route('/version/pkgname=<pkgname>/')
def version(pkgname):
    versions = db_get_versions(pkgname)
    return render_template('version.html', pkgname=pkgname, versions=versions)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
