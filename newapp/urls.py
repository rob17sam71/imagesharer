from django.urls import path
from .views import HomePageView, PostDetailView, AddFormView

app_name ='newapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/', AddFormView.as_view(), name='post'),
]