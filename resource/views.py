from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from .models import *
from .forms import VideoForm, SearchForm



def home (request):
    title = 'Hello there'
    return render(request, 'resource/home.html' , {'title':title})

def dashboard(request):

    return render (request, 'resource/dashboard.html')

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name= 'registration/signup.html'

    def form_valid(self, form):
        view = super(Signup, self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request,user)
        return view




class CreateSource(generic.CreateView):
    model = Source
    fields= ['title']
    template_name = 'resource/create_source.html'
    success_url= reverse_lazy ('dashboard')


    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateSource, self).form_valid(form)
        return redirect ('dashboard')


class DetailSource (generic.DetailView):
    model = Source
    template_name= 'resource/details.html'

class UpdateSource (generic.UpdateView):
    model = Source
    template_name= 'resource/update.html'
    fields= ['title']
    success_url= reverse_lazy('dashboard')

class DeleteSource (generic.DeleteView):
    model = Source
    template_name= 'resource/delete.html'
    success_url= reverse_lazy('dashboard')

def add_video(request, pk):
    form = VideoForm()
    search= SearchForm()

    if request.method == 'POST':
        data_form = VideoForm(request.POST)
        if data_form.is_valid():
            video = Video()
            video.url =data_form.cleaned_data['url']
            video.title =data_form.cleaned_data['title']
            video.youtube_id =data_form.cleaned_data['youtube_id']
            video.source = Source.objects.get(pk=pk)
            video.save()

    context ={
        'form':form,
        'search':search

    }
    return render(request, 'resource/addvideo.html', context)


