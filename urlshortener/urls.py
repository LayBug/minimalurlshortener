from django.urls import path
from . import views


urlpatterns = [
        path('', views.shorten_url, name = "homepage"),
        path('<slug:slug>/', views.redirect_page, name="redirect"),
        path('urls/<int:pk>/', views.UrlDetailView.as_view(), name = "success",),
        ]


