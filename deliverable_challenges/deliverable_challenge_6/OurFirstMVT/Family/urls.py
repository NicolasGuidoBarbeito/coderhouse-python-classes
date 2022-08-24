from django.urls import path
from .views import family_members, family_member_registration


urlpatterns = [
    path('', family_members),
    path('registration/<str:first_name>/<str:last_name>/<int:age>/<str:birthdate_as_string>', family_member_registration)
]
