# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

import uuid


class UserModel(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    last_request_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()



class PostModel(models.Model):
	user = models.ForeignKey(UserModel)
	image = models.FileField(upload_to='user_images')
	image_url = models.CharField(max_length=255)
	caption = models.CharField(max_length=240)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	has_liked = False



class LikeModel(models.Model):
	user = models.ForeignKey(UserModel)
	post = models.ForeignKey(PostModel)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)


class CommentModel(models.Model):
	user = models.ForeignKey(UserModel)
	post = models.ForeignKey(PostModel)
	comment_text = models.CharField(max_length=555)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)


def __str__(self):
	return self.user.username + ' said ' + self.comment.text


@property
def like_count(self):
	return len(LikeModel.objects.filter(post=self))


@property
def comments(self):
	return CommentModel.objects.filter(post=self).order_by('-created_on')

from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key= 'ed75fbbb16be4747ac79f8405e46f975')

model = app.models.get('food-items.v1.0')

response = model.predict_by_url(url='http://waterwipes.com/fr/wp-content/uploads/sites/6/2012/06/original_c2b07af8bc4ab73d8b45da0702f39be1.jpg')
print response