from flask import Blueprint,request,render_template,g,redirect,url_for
from .forms import QuestionForm,AnswerForm
from models import QuestionModel
from exts import db
from decorators import login_requried
from models import QuestionModel,AnwserModel

bp=Blueprint("qa",__name__,url_prefix='/')

@bp.route('/')
def index():
   #获取页码值,设定默认值
   page=request.args.get('page',1)

   questions = QuestionModel.query.order_by(QuestionModel.create_time.desc())

   # 返回一个分页器对象
   paginate = questions.paginate(page=int(page), per_page=20)
   # questions=QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
   return render_template('index.html',paginate=paginate)


@bp.route('/qa/public',methods=['GET','POST'])
@login_requried
def public_qa():
   if(request.method=='GET'):
      return render_template('public_question.html')
   else:
      form=QuestionForm(request.form)
      if form.validate():
         title=form.title.data
         content=form.content.data
         question=QuestionModel(title=title,content=content,author=g.user)
         db.session.add(question)
         db.session.commit()
         return redirect('/')
      else:
         print(form.errors)
         return redirect(url_for("qa.public_qa"))

@bp.route('/qa/detail/<int:qa_id>')
def detail(qa_id):
   qa=QuestionModel.query.get(qa_id)
   answers=''
   if qa.filename:
      answers=AnwserModel.query.filter_by(filename=qa.filename)
   return render_template('detail.html',question=qa,answers=answers)


@bp.route('/answer/public',methods=['POST'])
@login_requried
def public_answer():
   form=AnswerForm(request.form)
   if form.validate():
      content=form.content.data
      question_id=form.question_id.data
      answer=AnwserModel(content=content,question_id=question_id,author_id=g.user.id)
      db.session.add(answer)
      db.session.commit()
      return redirect(url_for('qa.detail',qa_id=question_id))

   else:
      print(form.errors)
      return redirect(url_for('qa.detail',qa_id=request.form.get("question_id")))


@bp.route('/search')
def search():
   # 获取页码值,设定默认值
   page = request.args.get('page', 1)
   q=request.args.get("q")
   questions=QuestionModel.query.filter(QuestionModel.title.contains(q))
   paginate=questions.paginate(page=int(page), per_page=10)
   return render_template('search.html',paginate=paginate,q=q)


