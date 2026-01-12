from home.views import index , person, login ,PersonAPI , PeopleViewSet, RegisterAPI, LoginAPI

from django.contrib import admin
from django.urls import path  , include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', PeopleViewSet, basename='people')
urlpatterns = router.urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view()),
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('login/', LoginAPI.as_view()),
    path('persons/', PersonAPI.as_view()),
]
