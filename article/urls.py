from django.conf.urls import url
from django.urls      import path, include
from article          import views





urlpatterns =[
       path('latest-articles/',views.LatestArticleList.as_view()),
       path('articles/search/', views.search),
       path('articles/<slug:article_slug>/',views.ArticleDetail.as_view()),
       

]