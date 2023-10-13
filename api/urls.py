from django.urls import path
from .views import*

urlpatterns =[
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
]