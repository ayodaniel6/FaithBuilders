from django.urls import reverse_lazy
from django.views import generic
from .forms import AppointmentForm, Client
from django.utils import timezone
from blog.models import Article
from .models import  Newsletter, Request

# Create your views here.

class HomePageView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'posts'
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published__lte=timezone.now()).order_by('-published')[:3]
    
    def newsletter(self, request):

        if request.method == 'POST':
            email = request.POST.get('email')
            email.save()

            Newsletter.objects.update()


class AboutPageView(generic.TemplateView):
    template_name = 'home/about.html'

    def Newsletter_method(self, request):

        if request.method == 'POST':
            email = request.POST.get('email')
            email.save()

            return Newsletter.objects.update()

class ContactPageView(generic.CreateView):
    model = Client
    template_name = 'home/contact.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('home:thanks')

    def Request_method(self, request):

        if request.method == 'POST':
            name = request.POST.get('name')
            request_ = request.POST.get('request')
            name.save()
            request_.save()

            return Request.objects.update()

class ThanksPageView(generic.TemplateView):
    template_name = 'home/thanks.html'


