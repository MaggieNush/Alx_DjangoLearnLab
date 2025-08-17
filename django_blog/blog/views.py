from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

def home_view(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')

    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'blog/profile_edit.html', {'form': form})

def login_user(request):
    return LoginView.as_view(template_name='blog/login.html')(request)

def logout_user(request):
    logout(request)
    return redirect('blog:home')

class PostListView(ListView):
    """
    Displays a list of all blog posts.
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """
    Views details of a specific blog post.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows users to create new blog posts.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form): # Overrides the form_valid method to automatically set the auther's name
        # Tells the form not to commit to the database
        form.instance.author = self.request.user
        # Saves the form before proceeding with the rest of the logic
        return super().form_valid(form)
    
