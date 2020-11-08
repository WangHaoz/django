from django.conf.urls import url

from CBV import views

urlpatterns = [
    url(r'^hello/', views.HelloCBV.as_view(msg='Sleeping'), name='hello'),
    url(r'^books/', views.BooksCBV.as_view(), name='books'),

    url(r'^helloview/', views.HelloView.as_view()),
    url(r'^template/', views.HelloTemplateView.as_view()),
    url(r'^listview/', views.HelloListView.as_view()),
]