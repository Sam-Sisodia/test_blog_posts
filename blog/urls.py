
from django.urls import path
from .  import views

urlpatterns = [
    path("",views.home,name='home'),
    path("sign-in",views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path("blogs/",views.Blogs, name= "blogs"),
    path("search-blog/",views.search_blogs,name="search-blog"),
    path("logout",views.logout_user, name='logout'),

    path("detail-page/<int:id>/",views.Blog_Detail, name="detail-page"),
    path("comment-blog/<int:id>/",views.Commnet_Blog,name="comment-blog"),
    path("share-page/<int:id>/",views.Share_Blogs,name="share-page"),
    path("view-blog/<str:token>/",views.View_blog,name="view-blog"),
    path("upload/",views.upload),
]
