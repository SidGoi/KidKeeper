from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("take-attendance/", views.take_attendance, name="take_attendance"),
    path("submit-attendance/", views.submit_attendance, name="submit_attendance"),
    path("view-attendance/", views.view_attendance, name="view_attendance"),
    path(
        "view-attendance/<str:date>/",
        views.attendance_by_date,
        name="attendance_by_date",
    ),
]
