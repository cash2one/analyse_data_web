#!/usr/bin/env python
# encoding: utf-8
from analyse_data import app,db
from analyse_data.models import Apps

# 往tb_apps中插入随机数据
def add_app():
    import random
    import string
    seed = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(10):
        A_string = "".join(random.sample(seed, random.randint(3, 6)))
        app_data = Apps(A_string, A_string, A_string, A_string)
        db.session.add(app_data)
        db.session.commit()



def get_all_Apps():
    apps = Apps.query.all()
    apps_in_json = []
    app_counter = 0
    for app in apps:
        apps_in_json.append({app_counter: app.as_dict()})
        app_counter += 1
    import json
    all_apps = json.dumps(apps_in_json)
    return all_apps


if __name__ == '__main__':
    # db.drop_all()
    print(Apps.query.all())