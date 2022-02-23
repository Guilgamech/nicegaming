from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('list/', views.listPost.as_view(), name='list'),
    path('createpost/', views.createPost.as_view(), name='create'),
    path('detailpost/<int:id_post>/', views.detailPost.as_view(), name='details'),
]