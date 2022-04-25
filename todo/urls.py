from django.urls import path
from rest_framework import routers

from todo import api

app_name='Todo'

router=routers.DefaultRouter()
router.register(r'api/todo',api.TodoViewSet,'todo')

urlpatterns=router.urls
