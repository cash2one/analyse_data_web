# encoding: utf-8
__author__ = 'fengshenjie'
from flask import render_template
import json
from flask import request, Response, make_response
from analyse_data import app


@app.route('/product_cmp/<string:a>/<string:b>/')
def product_cmp_ab(a, b):
    data = {'a': a,
            'b': b
            }
    header={'Content-type': 'application/json;charset=utf-8'}
    return json.dumps(data), 200, header

@app.route('/product_cmp/<string:a>/')
def product_cmp_testone(a):
    d={}
    return json.dumps(d)