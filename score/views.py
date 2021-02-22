from django.shortcuts import render
from .models import TakePicture
from .models import ChoosePicture
from .models import Result
from .forms import UploadFirst
from .forms import UploadSecond

from django.views import generic
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

        context = {
            'form': form
        }
        return render(request, 'score/choose_pic.html', context)

class ResultCreateView(generic.CreateView):
    model = Result
    template_name = "score/result.html"
    fields = '__all__'


