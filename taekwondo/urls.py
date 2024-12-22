from django.urls import path
from . import views

urlpatterns=[
#        path('',views.home, name='home'),
        path('',views.HomePageView.as_view(), name='home'),
        path('coaches/', views.CoachListView.as_view(), name='coaches-list'),
        path('detail/<int:pk>',views.CoachDetailView.as_view(),name='detail'),
        path('search/',views.search, name='search'),
        path('Coach/tambah',views.CoachCreateView.as_view(),name='create'),
        path('Coach/update/<int:pk>',views.CoachUpdateView.as_view(),name='update'),
        path('Coach/hapus/<int:pk>',views.CoachDeleteView.as_view(),name='delete'),
        path('daftar/',views.SignUpView.as_view(),name='signup')
]
  