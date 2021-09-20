from django.urls import path
from . import views

urlpatterns=[
#        path('',views.home, name='home'),
        path('',views.HomePageView.as_view(), name='home'),
#        path('detail/<int:id>',views.detail,name='detail'),
        path('detail/<int:pk>',views.PelatihDetailView.as_view(),name='detail'),
        path('search/',views.search, name='search'),
        path('Pelatih/tambah',views.PelatihCreateView.as_view(),name='create'),
        path('Pelatih/update/<int:pk>',views.PelatihUpdateView.as_view(),name='update'),
        path('Pelatih/hapus/<int:pk>',views.PelatihDeleteView.as_view(),name='delete'),
        path('daftar/',views.SignUpView.as_view(),name='signup')
]
