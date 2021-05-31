from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from .models import *
from .forms import VideoForm, SearchForm
from django.http import Http404 , JsonResponse
import urllib
from django.forms.utils import ErrorList
import requests

YOUTUBE_API_KEY= 'AIzaSyC4lcTzgTq_nmssqOJSYzJ5Uewn6Fbtz0U'



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
    source =Source.objects.get(pk=pk)
    if not source.user== request.user:
        raise Http404

    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.source= source
            video.url =form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id :
                video.youtube_id = video_id[0]
                response= requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={ YOUTUBE_API_KEY }')
                json = response.json()
                title = json['items'][0]['snippet']['title']
                video.title = title
                video.save()
                return redirect('detail_source',pk)
            else:
                errors= form._errors.setdefault('url', ErrorList())
                errors.append(" Its need to be a YouTube URL , Please check your url")

    context ={
        'form':form,
        'search':search,
        'source':source,

    }
    return render(request, 'resource/addvideo.html', context)




def video_search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        form = search_form.cleaned_data['search']

        return JsonResponse ({'hello':form})
    return JsonResponse ({'hello':'Not Working Rightnow'})
