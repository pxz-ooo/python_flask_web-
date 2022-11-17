#配置文件

SECRET_KEY='aadlslsllsss'

#mysql数据库配置
HOSTNAME='127.0.0.1'
PORT=3306
username='root'
password='root'
database='flask'

SQLALCHEMY_DATABASE_URI= f"mysql+pymysql://{username}:{password}@{HOSTNAME}:{PORT}/{database}?charset=utf8mb4"

#邮箱配置
MAIL_SERVER='smtp.qq.com'
MAIL_USE_SSL=True
MAIL_PORT=465
MAIL_USERNAME='2721206368@qq.com'
MAIL_PASSWORD='eyesqgardmdodech'
MAIL_DEFAULT_SENDER='2721206368@qq.com'

