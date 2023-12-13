from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, event_slot_edit_view

urlpatterns = [
    path('', main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("event_slots/add/", event_slot_edit_view, name="event_slots_add"),
    path("event_slots/<int:id>/", event_slot_edit_view, name="event_slots_edit")
]