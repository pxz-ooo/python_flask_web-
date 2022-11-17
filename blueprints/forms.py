import wtforms
from wtforms.validators import  DataRequired,Email,Length,EqualTo
from models import UserModel,Email_yanzhen
#用来验证前端数据是否符合要求
class RegesiterForm(wtforms.Form):
    email=wtforms.StringField(validators=[Email(message='邮箱格式错误')])
    captcha= wtforms.StringField(validators=[Length(min=6,max=6,message='验证码格式错误')])
    username = wtforms.StringField(validators=[Length(min=3,max=20,message='用户名格式错误')])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message='密码格式错误')])
    password_confirm=wtforms.StringField(validators=[EqualTo("password")])

    #自定义验证邮箱是否被注册以及验证码
    #判断邮箱是否已经被注册
    def validate_email(self,field):
        email=field.data
        user=UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message='该邮箱已经被注册')

    #判断验证码是否正确
    def validate_yanzhen(self,field):
        yanzhenma=field.data
        email=self.email.data
        yanzhen=Email_yanzhen.query.filter_by(email=email,yanzhenma=yanzhenma).first()
        if not yanzhen:
            raise wtforms.ValidationError(message='验证码错误')



class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message='邮箱格式错误')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误')])

class QuestionForm(wtforms.Form):
    title=wtforms.StringField(validators=[Length(2,100)])
    content=wtforms.StringField(DataRequired())

class AnswerForm(wtforms.Form):
    content=wtforms.StringField(DataRequired())
    question_id=wtforms.IntegerField(DataRequired())
