from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask import render_template
import templates as temp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/analyse_data?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class App(db.Model):
    __tablename__ = 'tb_apps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    developer = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    package = db.Column(db.String(100))

    def __init__(self, name, developer, description, package):
        self.name = name
        self.developer = developer
        self.description = description
        self.package = package

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<App %r>' % self.name


class Comment(db.Model):
    __tablename__ = 'tb_comment'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    market = db.Column(db.String(32))
    author = db.Column(db.String(32), nullable=True)
    score = db.Column(db.Integer)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, app_id, market, author, score, description, date):
        self.app_id = app_id
        self.market = market
        self.author = author
        self.score = score
        self.description = description
        self.date = date

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Record_day(db.Model):
    __tablename__ = 'tb_records_day'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    market = db.Column(db.String(32))
    version = db.Column(db.String(32), nullable=True)
    date = db.Column(db.DateTime)
    downloads_day = db.Column(db.Integer)

    def __init__(self, app_id, market, version, date, downloads_day):
        self.app_id = app_id
        self.market = market
        self.version = version
        self.date = date
        self.downloads_day = downloads_day

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Record_detail(db.Model):
    __tablename__ = 'tb_records_detail'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    market = db.Column(db.String(32))
    version = db.Column(db.String(32), nullable=True)
    tick = db.Column(db.DateTime)
    downloads_total = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Record_detail %r>' % self.app_id


class Score_sum(db.Model):
    __tablename__ = 'tb_score_sum'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    market = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    score = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Score_sum %r>' % self.app_id


class Version(db.Model):
    __tablename__ = 'tb_version_history'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    update_time = db.Column(db.DateTime)
    update_description = db.Column(db.Text, nullable=True)

    def __init__(self, name):
        self.name = name

    # 以字典格式返回所有表数据
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Version %r>' % self.app_id


@app.route('/hello_test')
def hello_world():
    # app_data = App('中邮钱包', '中邮消费金融有限公司', '没什么好描述的', 'com.youcash')
    record_data = Record_day(11, '应用宝', '2.0.1', '2017-01-01', 1000)
    db.session.add(record_data)
    db.session.commit()
    return 'hello'


# 往tb_apps中插入随机数据
def App_random_insert():
    import random
    import string
    seed = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(10):
        A_string = "".join(random.sample(seed, random.randint(3, 6)))
        app_data = App(A_string, A_string, A_string, A_string)
        db.session.add(app_data)
        db.session.commit()


# 以json形式返回整个tb_apps表
@app.route('/')
def get_all_Apps():
    apps = App.query.all()
    apps_in_json = []
    app_counter = 0
    for app in apps:
        apps_in_json.append({app_counter: app.as_dict()})
        app_counter += 1
    all_apps = json.dumps(apps_in_json)
    # return render_template('apps.html', all_apps=all_apps)
    return all_apps

if __name__ == '__main__':
    # print(get_all_Apps())
    app.run(debug=True)
