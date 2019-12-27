from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_view),
    # ex: /quotes/5/
    path('<int:quote_id>/', views.single_view, name='detail')
]
