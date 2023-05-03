from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
