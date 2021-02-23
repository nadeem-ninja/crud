from django.urls import path

from medical.views import medical_view, delete_medicine, add_medicine, update_view

urlpatterns = [
    path('', medical_view, name='medical'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
    path('add/', add_medicine, name='add_medicine'),
    path('update/<int:pk>/', update_view, name='update_view'),
]
