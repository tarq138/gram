from django.shortcuts import render, get_object_or_404
from .models import Profile


def userpage(request):
    users = Profile.objects.all()
    return render(request, "user.html", {"users" : users})
