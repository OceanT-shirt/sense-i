from django.urls import path

from .import views

app_name = 'score'
urlpatterns = [
    path('takepic', views.TakeCreateView.as_view(), name='take_pic'),
    path('choosepic', views.ChooseCreateView.as_view(), name='choose_pic'),

]

# urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
