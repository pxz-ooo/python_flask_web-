from flask import Flask,session,g
import config
from exts import db,mail
from blueprints.qa import bp as qa_bp
from blueprints.user import  bp as user_bp
from flask_bootstrap import  Bootstrap4
from models import UserModel
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config)
bootstrap=Bootstrap4(app)

db.init_app(app)
migrate=Migrate(app,db)
mail.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def mybefore_request():
    user_id=session.get('user_id')
    if user_id:
        user=UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)

@app.context_processor
def my_context_processor():
    return {"user":g.user}


if __name__ == '__main__':
    app.run()
