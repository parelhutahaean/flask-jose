from flask import Flask,render_template,url_for,flash,redirect,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash('You just changed your breed to: {}'.format(session['breed']))
        return redirect(url_for('index'))
    return render_template('03-index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
