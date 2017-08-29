from analyse_data import db


class Apps(db.Model):
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
    def get_dict(self):
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
    def get_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RecordsDay(db.Model):
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
    def get_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RecordsDetail(db.Model):
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
    def get_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Record_detail %r>' % self.app_id


class Score(db.Model):
    __tablename__ = 'tb_score_sum'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    market = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    score = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name

    # 以字典格式返回所有表数据
    def get_dict(self):
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
    def get_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Version %r>' % self.app_id
