from django import forms
from .models import Document

# from PIL import Image


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'photo', )


class DisplayPicForm(forms.Form):
    image = forms.ImageField()

something.html (you name this file)

{% extends 'Instagram/base.html' %} {% block content %}
<form method="post" enctype="multipart/form-data">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
{% endblock %}