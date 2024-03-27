from django.urls import path
from .views import PostList, NewsDetail, SearchList, NewCreateView, PostUpdate, PostDelete


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

]