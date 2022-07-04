from django.shortcuts import render
from . models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html', {'posts': posts})
    
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})


def blog_detailView(request, slug): # so as to view the full blog post- the function is taking in 2 arguments i.e the request and the slug
    post = Post.objects.get(slug = slug) # we are fetching posts from the db by their slug
    comments = post.comments.all() # we are fetching all the comments for a particular blog post. This was possible becoz we put related_name of comments in our models.py
    new_comment = None # the new comment that the user is about to put in
    
    if request.method == 'POST':
        form = CommentForm(request.POST) #request.POST stands for the data that the user has put in the form
        if form.is_valid(): # if the content of the form is valid and okay
            new_comment = form.save(commit=False)# the comment won't hit the database yet
            new_comment.post = post # the new comment should be for the current post
            new_comment.save()# now the new comment can be saved to the db
            return HttpResponseRedirect(reverse('blog_detail', args = [str(post.slug)]))# so that it returns a fresh new detail of that particular post after someone has finished adding the comment
            
    else:
        form = CommentForm()# if it isn't a post request, just return an empty form
    

    return render(request, 'blog_detail.html', {'post': post,'form': form, 'comments':comments, 'new_comment':new_comment})

