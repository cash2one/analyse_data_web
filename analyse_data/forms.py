from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    # 无需任何配置，Form 是一个带有 CSRF 保护的并且会话安全的表单
    appname = StringField('应用名称', validators=[DataRequired()])
    submit = SubmitField('搜索')
