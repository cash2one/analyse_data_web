from flask import render_template
import json
from flask import request
from analyse_data import app


@app.route('/hello/')
def hello_world():
    url = request.args
    return render_template('hello.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/product_cmp/')
def product_cmp():
    return render_template('product_cmp.html')


@app.route('/user/<name>')
def user(name):
    return render_template('base.html', name=name)

@app.route('/downloads/total/<pkgname>/')
def totaldownloads():
    return render_template('totaldownloads.html')

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
    a={}
    return render_template('version.html', pkgname=pkgname, mydict=a)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
