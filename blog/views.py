from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import UserPostForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

class DashboardView(generic.TemplateView):
    template_name = 'blog/dashboard.html'
    

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    form_class = UserPostForm
    template_name = 'blog/post_form.html'
    model = Article
    success_url = 'blog:post_detail'


class DraftView(LoginRequiredMixin,generic.ListView):
    model = Article
    redirect_field_name = 'blog/post_list.html'
    template_name = 'blog/draft.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Article.objects.filter(published__isnull=True).order_by('-created')
    

class PostListView(generic.ListView):
    model = Article
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Article.objects.filter(published__lte=timezone.now()).order_by('-published')


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Article
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Article
    redirect_field_name = 'blog/post_detail.html'
    form_class = UserPostForm
    template_name = 'blog/post_form.html'


class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Article
    context_object_name = 'post'
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

def PostPublishView(request,pk):
    post = get_object_or_404(Article, pk=pk)
    post.publish()
    return redirect(reverse('blog:post_detail', kwargs={'pk':post.pk}))


def StaffLoginView(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        login(request, user)
        return redirect('blog:dashboard')

    return render(request, 'registration/login.html')


@login_required
def StaffLogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home:home'))


