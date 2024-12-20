from django.urls import path
from . import views

urlpatterns=[
#        path('',views.home, name='home'),
        path('',views.HomePageView.as_view(), name='home'),
        path('coaches/', views.PelatihListView.as_view, name='coaches-list'),
        path('detail/<int:pk>',views.PelatihDetailView.as_view(),name='detail'),
        path('search/',views.search, name='search'),
        path('Pelatih/tambah',views.PelatihCreateView.as_view(),name='create'),
        path('Pelatih/update/<int:pk>',views.PelatihUpdateView.as_view(),name='update'),
        path('Pelatih/hapus/<int:pk>',views.PelatihDeleteView.as_view(),name='delete'),
        path('daftar/',views.SignUpView.as_view(),name='signup')
]
