from django.urls import path, include

from world_of_speed.cars.views import CarCreateView, CarListview, CarDetailView, CarEditView, CarDeleteView

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('catalogue/', CarListview.as_view(), name='catalogue'),
    path('<int:pk>/', include([
        path('details/', CarDetailView.as_view(), name='detail-car'),
        path('edit/', CarEditView.as_view(), name='edit-car'),
        path('delete/', CarDeleteView.as_view(), name='delete-car'),
    ])),

]
