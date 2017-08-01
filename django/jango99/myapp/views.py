# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, PostForm, LikeForm, CommentForm
from .models import UserModel, SessionToken,  PostModel, LikeModel, CommentModel
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta
from django.utils import timezone
from settings import BASE_DIR

from imgurpython import ImgurClient

CLIENT_ID = '0ab4ef1534b7057'
CLIENT_SECRET = '7068b7fc10bea81015206e47b476575a2c3fdead'


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # saving data to DB
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
            return render(request, 'success.html',{'form':form})
        else:
            print 'Invalid Data'
            return redirect('login/')
    elif request.method == 'GET':
        form = SignUpForm()
        return render(request, 'index.html', {'form': form})


def login_view(request):
    response_data = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username).first()
            print 'user found'

            if user:
                if check_password(password, user.password):
                   print 'Verified'
                   token = SessionToken(user=user)
                   token.create_token()
                   token.save()
                   response = redirect('feed/')
                   response.set_cookie(key='session_token', value=token.session_token)
                   return render(request, 'feed.html',{'form':form})
                else:
                    print 'Wrong Something!'
                    return render(request, 'error.html')
        else:
            print 'form invalid'

    elif request.method == 'GET':
        form = LoginForm()
      #  response_data['form'] = form
    return render(request, 'login.html', {'form' : form})


def post_view(request):
    user = check_validation(request)

    if user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                post = PostModel(user=user, image=image, caption=caption)
                post.save()

                path = str(BASE_DIR + post.image.url)

                client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
                post.image_url = client.upload_from_path(path, anon=True)['https://imgur.com/2AHqxxc']
                post.save()

                return redirect('/feed/')

        else:
            form = PostForm()
        return render(request, 'post.html', {'form': form})
    else:
        return redirect('login/')


def feed_view(request):
    user = check_validation(request)
    if user:

        posts = PostModel.objects.all().order_by('created_on')

        for post in posts:
            existing_like = LikeModel.objects.filter(post_id=post.id, user=user).first()
            if existing_like:
                post.has_liked = True

        return render(request, 'feed.html', {'posts': posts})
    else:

        return redirect('login/')


def like_view(request):
    user = check_validation(request)
    print 'Like View Called'
    if user and request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id

            existing_like = LikeModel.objects.filter(post_id=post_id, user=user).first()
            print 'Validation Sucessfull'

            if not existing_like:
                LikeModel.objects.create(post_id=post_id, user=user)

            else:
                existing_like.delete()
            return redirect('/feed/')
    else:
        return redirect('/login/')


def comment_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            comment_text = form.cleaned_data.get('comment_text')
            comment = CommentModel.objects.create(user=user, post_id=post_id, comment_text=comment_text)
            comment.save()
            return redirect('/feed/')
        else:
            return redirect('/feed/')
    else:
        return redirect('/login')


# For validating the session
def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            time_to_live = session.created_on + timedelta(days=1)
            if time_to_live > timezone.now():
                return session.user
    else:
        return None