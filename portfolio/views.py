from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Person.objects
    return render (request, 'portfolio/home.html', {'posts':posts})
def detail(request, post_id):
        post_detail = get_object_or_404(Person, pk = post_id)
        return render (request, 'portfolio/detail.html', {'post':post_detail})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect ('detail', post_id=post.pk)
    else:
        form = PostForm()
        return render(request, 'portfolio/new.html', {'form':form})
def post_edit(request, post_id):
    post=get_object_or_404(Person,pk=post_id)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form=PostForm(instance=post)
        return render(request, 'portfolio/edit.html', {'form': form})
def post_delete(request, post_id):
    post=get_object_or_404(Person, pk=post_id)
    post.delete()
    return redirect('home')