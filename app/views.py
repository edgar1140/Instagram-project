from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from .forms import AddPicForm
from app.models import Document
from app.forms import Filters
from PIL import Image


def make_obj(picture):
    comments = []
    comment_set = picture.comment_set.all()
    for c in comment_set:
        comments.append(c.comment)
    return {
        'url': picture.photo.url.replace('Instagram/static', ''),
        'description': picture.description,
        'id': picture.id,
        'comments': comments
    }


class PicView(View):
    def get(self, request):
        picture_objects = models.Document.objects.all()
        pictures = []
        for picture in picture_objects:
            pictures.append(make_obj(picture))

        return render(request, 'Instagram/feed.html',
                      {'pictures': pictures,
                       'post_comment': CommentForm()})


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


class InsertComment(View):
    def post(self, request, image_id):
        pic = models.Document.objects.get(id=image_id)
        form = CommentForm(pic, request.POST)
        if form.is_valid():
            form.saveComment()
            return redirect('Instagram:feed')
        else:
            return redirect('Instagram:feed')
