from django.urls import path

from . import views

urlpatterns = [
    path('get_test', views.getTest),
    path('add_test', views.addTest),
    path('detect_face', views.face_detection),
    path('rec_face', views.recognizeFace),
    path('get_face', views.getFace),
]
