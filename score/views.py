from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
from .models import TakePicture, Result, ChoosePicture
from .forms import UploadFirst, UploadSecond
from django.views import generic
import base64
import cv2
import numpy as np
# Create your views here.

class TakeCreateView(generic.CreateView):
    model = TakePicture
    template_name = "score/take_pic.html"
    fields = '__all__'

    def edit_take_pic(request):
        if request.method != 'POST':
            form = UploadFirst()
        else:
            form = UploadFirst(request.POST, request.FILES)
            if form.is_valid():
                take_pic = form.cleaned_data['take_pic']
                take_picture = TakePicture()
                take_picture.take_pic = take_pic
                take_picture.save()

        context = {
            'form': form
        }
        return render(request, 'score/choose_pic.html', context)




class ChooseCreateView(generic.CreateView):
    model = ChoosePicture
    template_name = "score/choose_pic.html"
    fields = '__all__'

    def edit_choose_pic(request):
        if request.method != 'POST':
            form = UploadSecond()
        else:
            form = UploadSecond(request.POST, request.FILES)
            if form.is_valid():
                choose_pic = form.cleaned_data['choose_pic']
                choose_picture = ChoosePicture()
                choose_picture.choose_pic = choose_pic
                choose_picture.save()
                request.session['form_data'] = request.POST

        context = {
            'form': form
        }
        return render(request, 'score/choose_pic.html', context)

class ResultCreateView(generic.CreateView):
    model = Result
    template_name = "score/result.html"
    fields = '__all__'

def ImageUpload(request):
    if request.method == 'POST':
        print(list(request.POST.items()))
        print(dict(request.POST.items()))
        print(dict(request.FILES))
        posted_img = request.FILES['image']
        image = request.POST.get("image")
        image2 = dict(request.POST.items())["image"]
        new_image = Image.objects.create(image=posted_img)

        img_data = base64.b64decode(image)
        img_np = np.fromstring(img_data, np.uint8)
        src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)

        print(src)

        return HttpResponse(new_image.image.url)




