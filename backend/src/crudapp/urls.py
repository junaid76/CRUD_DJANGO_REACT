from crudapp.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from crudapp import views


router = DefaultRouter()
router.register(r'movies',views.MovieViewSet,basename='movie')
urlpatterns = router.urls
