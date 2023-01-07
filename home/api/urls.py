from django.urls import include, path
from rest_framework import routers
from home.views import views

router = routers.DefaultRouter()
router.register(r'Trainer', views.TrainerViewSet)
router.register(r'Vet', views.VetViewSet)
router.register(r'Dog_info', views.Dog_infoViewSet)
router.register(r'Places', views.PlacesViewSet)
router.register(r'Breed_info', views.Breed_infoViewSet)
router.register(r'Product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
    
]
