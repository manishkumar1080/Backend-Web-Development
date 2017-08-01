# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserModel)
admin.site.register(models.PostModel)
admin.site.register(models.SessionToken)
admin.site.register(models.CommentModel)
admin.site.register(models.LikeModel)


