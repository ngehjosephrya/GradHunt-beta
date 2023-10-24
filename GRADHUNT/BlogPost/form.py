from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':20,}))
    class Meta:
        model = Post
        fields = ['title','content', 'image']
        
        