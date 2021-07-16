from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_uploads import UploadSet, IMAGES,configure_uploads
from flask_wtf.file import FileAllowed, FileField, FileRequired
set_mypic = UploadSet('mypic')
class UploadForm(FlaskForm):
    # 文件field设置为‘必须的’，过滤规则设置为‘set_mypic’
    upload = FileField('image', validators=[FileRequired(), FileAllowed(set_mypic, 'you can upload images only!')])
    submit = SubmitField('ok')