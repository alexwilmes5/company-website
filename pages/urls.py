from django.urls import path

from .views import home_page_view, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view()),
    path("", home_page_view),
]