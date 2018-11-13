from django.shortcuts import render, get_object_or_404, redirect
from .models import ProfileImage, Profile
from .forms import AddImage
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Q


def userpage(request):
    users = Profile.objects.all()
    images = ProfileImage.objects.filter()
    #query = request.GET.get('q')
    # if query != "":
    #     founded_profiles = User.objects.filter(Q(username__icontains=query))
    # else:
    #     founded_profiles = ''
    if request.user.id != None:
        profile = get_object_or_404(Profile, id=request.user.id)
    else:
        profile = ""
    form = AddImage()
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():

            form = form.save(commit=False)
            form.profile = request.user.profile
            form.save()
            return redirect(userpage)
    else:
        form = AddImage()
    return render(request, "user.html", {"users": users,
                                         "images": images,
                                         "profile": profile,
                                         "form": form})


def search(request):
    query = request.GET.get('q')
    if query != "":
        founded_users = User.objects.filter(Q(username__icontains=query))
    else:
        founded_users = ''
    #founded_profiles = ''
    #for founded_user in founded_users:

    return render(request, "user.html", {'founded_users': founded_users})
