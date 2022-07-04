"""Members App URLs - Catholic App"""
from django.urls import path
from members import views

urlpatterns = [
    path('', views.member_home, name='member_home'),
    path('member_profile/', views.member_profile, name="member_profile"),

    # path('<int:member_id>/<str:member_email_address>',
    #     views.member_profile, name='member_profile'),
    # path('search', views.search, name='search'),
]
