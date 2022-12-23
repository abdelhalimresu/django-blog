from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    # image = forms.ImageField(allow_empty_file=True, required=False)
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')