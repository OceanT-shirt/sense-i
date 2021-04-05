from django.urls import path
from django.contrib.staticfiles.urls import static
from sense_i import settings
from .views import ChooseCreateView, TakeCreateView, ResultCreateView
from .views import ImageUpload


from .import views

app_name = 'score'
urlpatterns = [
    path('takepic', TakeCreateView.as_view(), name='take_pic'),
    path('choosepic', ChooseCreateView.as_view(), name='choose_pic'),
    path('result', ResultCreateView.as_view(), name='result'),
    path('imgupload', views.ImageUpload, name='imgupload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
