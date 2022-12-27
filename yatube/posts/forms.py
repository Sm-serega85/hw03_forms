from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
            label=Post._meta.get_field("text").verbose_name,
            help_text=Post._meta.get_field("text").help_text)

    class Meta:
        model = Post
        fields = ('text', 'group')
