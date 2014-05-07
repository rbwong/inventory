from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
#from bulletin.models import Topic, Board, Thread, Post
#from bulletin.forms import BoardCreationForm, ThreadCreationForm, PostCreationForm

@login_required
def hello_world(request):
    return HttpResponse("Hello, world.")