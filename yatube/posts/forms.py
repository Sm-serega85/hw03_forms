from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'group')
        label = {'text': 'Пост',
                 'group': 'Группа'}
        help_text = {'text': 'Новый пост',
                     'group': 'Группа с текущим постом'}
