from django.urls import path
from blog import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<int:blog_id>/<str:blog_slug>',
         views.blogarticle, name='blogarticle'),
    # path('search', views.search, name='search'),
]
