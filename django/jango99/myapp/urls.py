from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.signup_view),
    url(r'login/',views.login_view),
    url(r'post/',views.post_view),
    url(r'feed/',views.feed_view),
    url(r'like/',views.like_view),
    url(r'comment',views.comment_view)

]