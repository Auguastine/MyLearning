from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
   name = StringField('What is your name?',validators=[DataRequired()])
   submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())
    

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


