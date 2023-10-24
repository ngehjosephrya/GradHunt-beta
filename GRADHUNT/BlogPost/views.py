from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .form import PostForm

class IndexView(View):
    template_name = 'BlogPost/index.html'
    
    def get(self, request):
        posts = Post.objects.all()
        form = PostForm()
        context = {
            'posts': posts,
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('BlogPost:blogpost') 
        else:
            posts = Post.objects.all()
            context = {
                'posts': posts,
                'form': form
            }
            return render(request, self.template_name, context)
