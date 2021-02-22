from django.contrib import admin
from .models import ChoosePicture
from .models import TakePicture
from .models import Result

# Register your models here.

admin.site.register(ChoosePicture)
admin.site.register(TakePicture)
admin.site.register(Result)
