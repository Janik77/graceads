from django.urls import path
from .views import *


urlpatterns = [
    path("", main_page_view),
    path("services/", services_page_view),
    path("about_us/", about_us_page_view),

    path("admin/", admin_page_view)
]
