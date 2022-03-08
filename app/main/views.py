from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import CommentForm,UpdateProfile,PitchesForm
from ..models import Pitches, Comments,User
from flask_login import login_required, current_user
from .. import db,photos
from wtforms import form
# from models import Pitches,Comments,User,PhotoProfile
import markdown2  


@main.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    # pitches_we_have = Pitches.query.order_by('id').all()
    # ,our_pitches=pitches_we_have
    

    main_title = 'These are piches we have, contribute to these'
    return render_template('index.html', main_title=main_title)

@main.route('/pickup_lines')
def pickup_lines():
    """
    view pitch function that returns pitch details and its data
    """
    title = "This is a pitch  page"
    pitch = Pitches.get_pitches("pickup_lines")
    return render_template('pickup_lines.html', title=title,pickup_pitch=pitch)

@main.route('/interviews')
def interviews():
    """
    view pitch function that returns pitch details and its data
    """
    title = "This is a pitch  page"
    pitch = Pitches.get_pitches('interview')
    return render_template('interviews.html', title=title,interview_pitch=pitch)

@main.route('/products')
def products():
    """
    view pitch function that returns pitch details and its data
    """
    title = "This is a pitch  page"
    pitch = Pitches.get_pitches("products")
    return render_template('products.html', title=title,product_pitch=pitch)

@main.route('/promotion')
def promotions():
    """
    view pitch function that returns pitch details and its data
    """
    title = "This is a pitch  page"
    pitch = Pitches.get_pitches('promotion')
    return render_template('promotion.html', title=title,promotion_pitch=pitch)

@main.route('/pitches/new',methods= ['GET','POST'])
@login_required
def new_pitch():
    form = PitchesForm()

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitch = form.pitch.data

        new_pitch = Pitches(title=title,category=category, pitch=pitch)
        db.session.add(new_pitch)
        db.session.commit()
        # new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    page_tittle="create new pitch"
    return render_template("new_pitch.html",pitch_form=form,page_tittle=page_tittle)


@main.route('/comments/<int:id>',methods = ['GET','POST'])
def comments(id):
    """
    pitch comment function that returns comment details
    """
    title="This pitch's comments"
    comment=Comments.get_comments(id)
    pitch=Pitches.getPitchId(id)
    pitch_id=pitch.id
    
    return render_template('comments.html',title=title,pitch_comments=comment,pitch_id=pitch_id,pitch=pitch)
@main.route('/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    pitch=Pitches.getPitchId(id)
    comments = Comments.get_comments(id)
    form = CommentForm()
    pitch_id=pitch.id
    
    if form.validate_on_submit():
        # title = form.title.datatitle=title,
        comments = form.user_comment.data

        # Updated review instance
        new_comment = Comments(comment=comments)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('main.comments',id = pitch_id ))

    
    return render_template('new_comment.html',comment_form=form,comments=comments,pitch_id=pitch_id)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))









   
