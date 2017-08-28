from flask import render_template
import json
from flask import request, redirect
from analyse_data import app
from analyse_data.controller import *


@app.route('/hello/')
def hello():
    url = request.args
    return render_template('hello.html', name='fsj')


@app.route('/')
def index():
    apps = db_get_tb_apps()
    return render_template('index.html', apps=apps)


@app.route('/product_cmp/')
def product_cmp():
    return render_template('product_cmp.html')


@app.route('/downloads/total/<string:pkgname>/')
def totaldownloads(pkgname):
    records=db_get_totaldownloads(pkgname)
    appname=get_appname_by_pkgname(pkgname)
    return render_template('totaldownloads.html',
                           pkgname=pkgname, appname=appname, records=records)

@app.route('/downloads/daily/')
def dailydownloads():
    return redirect('/404')

@app.route('/comments/<pkgname>/')
def comments(pkgname):
    return render_template('comments.html')

@app.route('/monitoring/<pkgname>/')
def monitoring(pkgname):
    return redirect('/404')

@app.route('/keywords/<pkgname>/')
def keywords(pkgname):
    return redirect('/404')

@app.route('/version/<pkgname>/')
def version(pkgname):
    appname=get_appname_by_pkgname(pkgname)
    versions=db_get_versions(pkgname)
    return render_template('version.html', appname=appname,
                           pkgname=pkgname, versions=versions)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
