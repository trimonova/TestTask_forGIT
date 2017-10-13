from django.conf.urls import url
from hello import views
urlpatterns = [
    url(r'^menu/', views.menu, name='menu'),
    url(r'^order/create/?', views.order, name='order'),
    url(r'^login/?', views.user_login, name='user_login'),
]
