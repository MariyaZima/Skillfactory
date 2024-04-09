from django.urls import path
from .views import PostList, NewsDetail, SearchList, NewCreateView, PostUpdate, PostDelete, BaseRegisterView, \
   IndexView
from django.contrib.auth.views import LoginView, LogoutView
from .views import upgrade_me


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
   path('search/', SearchList.as_view(), name='post_search'),
   path('create/', NewCreateView.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', NewCreateView.as_view(), name='post_article_create'),
   path('article/<int:pk>/edit/', PostUpdate.as_view(), name='post_article_update'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='post_article_delete'),
   path('index/', IndexView.as_view(template_name='index.html'), name='index'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
   path('upgrade/', upgrade_me, name='upgrade')

]