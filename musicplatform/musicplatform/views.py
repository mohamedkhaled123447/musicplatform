import http
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate

class signin(View):
    def get(self,request):
        return render(request, 'signin.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if(user is not None):
            return redirect('create_artist')    
        else:
            return redirect('artists')          
