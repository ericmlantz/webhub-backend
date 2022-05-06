from django.urls import path
from . import views

urlpatterns = [

# User Paths
    path('', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

# Interest Paths
    path('interests/', views.InterestList.as_view(), name='interest_list'),
    path('interests/<int:pk>', views.InterestDetail.as_view(), name='interest_detail'),

# Page Paths
    path('pages/', views.PageList.as_view(), name='page_list'),
    path('pages/<int:pk>', views.PageDetail.as_view(), name='page_detail'),

# Search Paths
    path('searches/', views.SearchList.as_view(), name='search_list'),
    path('searches/<int:pk>', views.SearchDetail.as_view(), name='search_detail'),

# Notes Paths 
    path('notes/', views.NoteList.as_view(), name='note_list'),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name='note_detail'),
]