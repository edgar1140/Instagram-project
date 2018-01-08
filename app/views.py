from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from .forms import AddPicForm
from app.models import Document
from app.forms import Filters
from PIL import Image


class PicFilter(View):
    def get(self, request, image_id):
        form = Filters()
        path = 'app/static/' + Document.objects.get(id=image_id).image_url()
        return render(request, 'Instagram/feed.html', {'form': form})

    def post(self, request, image_id):
        form = Filters(request.POST)
        path = 'app/static/' + Document.objects.get(id=image_id).image_url()
        image = Image.open(path)
        if form.is_valid():
            f = form.apply_filter()
            image.convert('RGB').filter(f).save(path)
            return redirect('Instagram:feed')
        return render(request, 'Instagram/PicFilters.html', {'form': form})


def display_pic(request):
    pictures = Document.objects.all()
    return render(request, 'Instagram/feed.html', {'pictures': pictures})


def add_pic(request):
    form = AddPicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Instagram:feed')
    else:
        return render(request, 'Instagram/upload.html', {'form': form})


class AddComment(forms.Form):
    comment = forms.CharField()

    def __init__(self, document=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document = document

    def saveComment(self):
        return self.document.comment_set.create(
            comment=self.cleaned_data['comment'])