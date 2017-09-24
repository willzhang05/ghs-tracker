from django.conf.urls import url

from .views import request_hours, add_hour_item, edit_hour_item, approve_hours

urlpatterns = [
    url(r'^request/', request_hours, name='request_hours'),
    url(r'^add_item/', add_hour_item, name='add_hour_item'),
    url(r'^edit_item/(?P<item>[0-9]+)', edit_hour_item, name='edit_hour_item'),
    url(r'^approve/', approve_hours, name='approve_hours'),
]
