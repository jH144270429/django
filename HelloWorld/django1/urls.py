from django.conf.urls import url
from. import hello
from message import views
urlpatterns = [
    url(r'^hello/$',hello.hello),
    url(r'^form/$',views.getform),
]


