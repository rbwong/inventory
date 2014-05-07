from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = form.data['username']
        password = form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponseRedirect('/')
    else:
    	form = AuthenticationForm()
        return render_to_response('auth/login.html', {'form': form}, context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')