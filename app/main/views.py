from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import BlogForm, UpdateProfile, CommentForm
from flask_login import login_required, current_user
from ..models import User, Comment, Upvote, Downvote, Post, Subscriber, Quote
from .. import db, photos
from ..requests import get_quote


#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    Quote = get_quote()
    title = 'iBlog.com'
    return render_template('index.html',  title = title, Quote=Quote)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user)


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

    return render_template('profile/update.html',form=form)

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

@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        return ('not found')
    return render_template('profile.html', user=user)


@main.route('/user/<name>/profile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        error = 'The user does not exist'
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/profile.html', form=form)


@main.route('/blogs')
@login_required
def blog():
    blogs = Post.query.all()
    likes = Upvote.query.all()
    return render_template('blogs_display.html', blogs=blogs, likes=likes, user=user)

@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    View iBlog page function that returns the iBlog details page and its data
    '''
    title = 'iBlog.com'
    #date_created = blog.date_created.strftime('%b %d, %Y')
    
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post= form.post.data
        user_id = current_user._get_current_object().id
        post_obj = Post(post=post, title=title, user_id=user_id)
        post_obj.save()
        return redirect(url_for('main.blog'))
    return render_template('new_blog.html', form=form)



@main.route('/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    #date_created = blog.date_created.strftime('%b %d, %Y')
    form = CommentForm()
    post = Post.query.get(post_id)
    user = User.query.all()
    comments = Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            post_id=post_id,
            user_id=user_id,
            )

        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return redirect(url_for('.comment', post_id=post_id))
    return render_template('comment.html', form=form, post=post, comments=comments, user=user)



@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def upvote(id):
    post = Post.query.get(id)
    vote_mpya = Upvote(post=post, upvote=1)
    vote_mpya.save()
    return redirect(url_for('main.blog'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
    post = Post.query.get(id)
    vm = Downvote(post=post, downvote=1)
    vm.save()
    return redirect(url_for('main.blog'))


@main.route('/blog/comment/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comments = Comment.query.filter_by(id=id).first()
    post_id = comment.blog
    Comment.delete_comment(id)
    return redirect(url_for('main.blog',id=post_id))