from django.urls import path

from web.views import main_veiw

urlpatterns = [
    path('', main_veiw),
]