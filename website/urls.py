from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("send", views.send, name="send"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("review", views.review, name="review"),
    path("message", views.message, name="message"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("log_out", views.log_out, name="log_out"),
]