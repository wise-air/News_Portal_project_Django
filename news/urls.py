from django.urls import path

from .views import PostList, PostSearch, PostDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete #create_news


urlpatterns = [
   path('', PostList.as_view(), name='posts_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:id>', PostDetail.as_view(), name='post_details'),
   # path('news/create/', create_news, name='news_create'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('news/<int:id>/update/', NewsUpdate.as_view(), name='news_update'),
   path('article/<int:id>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('news/<int:id>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('article/<int:id>/delete/', ArticleDelete.as_view(), name='article_delete'),

]