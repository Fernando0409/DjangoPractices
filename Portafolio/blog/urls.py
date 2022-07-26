from django.urls import path
from .views import renderPost, postDetail

app_name = 'blog'

urlpatterns = [
     path('', renderPost, name='post'),
     # Recibe un parametro a la URL de tipo int
     path('<int:postID>', postDetail, name="postDetail")
]

