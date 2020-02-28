from django.apps import AppConfig


class DataModelAppConfig(AppConfig):
    name = 'data_model_app'


from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)