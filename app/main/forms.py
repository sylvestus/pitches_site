from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PitchesForm(FlaskForm):
    
    title = StringField('Pitch title',validators=[DataRequired()])
    category = SelectField('Category',
                                 choices=[('Select category','Select category'),('pickup_lines', 'pickup_lines'),('interview', 'interview'),('products', 'products'),('promotion', 'promotion')],
                                 validators=[DataRequired()])
    pitch= TextAreaField('Enter pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('More about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    user_comment = TextAreaField('comment on this pitch.')
    submit = SubmitField('Comment')