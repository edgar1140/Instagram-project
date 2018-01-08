from django.urls import path
from . import views

app_name = 'Instagram'

urlpatterns = [
    path('upload/', views.add_pic, name='upload'),
    path('feed/', views.display_pic, name='feed'),
    path('filter/<image_id>', views.PicFilter.as_view(), name='filter'),
    path('comment/<image_id>', views.InsertComment.as_view(), name='comment'),
]