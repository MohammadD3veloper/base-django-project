from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', views.ListPostsView.as_view(), name="list"),
    path('post/detail/<str:slug>/', views.DetailPostView.as_view(), name="detail"),
    path('post/search', views.SearchListView.as_view(), name="search"),
    path('dashboard',views.dashboardview, name="dashboard"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus',views.contactus,name='contactus'),
]