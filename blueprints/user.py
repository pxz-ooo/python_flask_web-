from flask import Blueprint,render_template,request,jsonify,redirect,url_for,session
from exts import mail,db
from flask_mail import Message
from models import Email_yanzhen
from .forms import RegesiterForm,LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash,check_password_hash
import string
import random

bp=Blueprint("user",__name__,url_prefix="/user")

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        form=LoginForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            user=UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for('user.login'))

            else:
                if check_password_hash(user.password,password):
                    session['user_id']=user.id
                    return redirect('/')
                else:
                    print('密码错误')
                    return redirect(url_for('user.login'))
        else:
            return redirect(url_for('user.login'))



@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        form=RegesiterForm(request.form)
        if form.validate():
            email=form.email.data
            username=form.username.data
            password=form.password.data
            user=UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))

        else:
            print(form.errors)
            return redirect(url_for('user.register'))


@bp.route('/mail/yanzhen')
def mail_yanzhen():
    email=request.args.get('email')
    source=string.digits*6
    yanzhenma=random.sample(source,6)
    yanzhenma=''.join(yanzhenma)
    message = Message(subject='邮箱注册验证码', recipients=[email], body=f"你的验证码为:{yanzhenma}")
    mail.send(message)
    # 用数据库方式存储
    email_yanzhen=Email_yanzhen(email=email,yanzhenma=yanzhenma)
    db.session.add(email_yanzhen)
    db.session.commit()
    return jsonify({"code":200,"message":"","data":None})

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')