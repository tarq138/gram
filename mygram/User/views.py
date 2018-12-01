from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import ProfileImage, Profile
from .forms import AddImage
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q


users = Profile.objects.all()
images = ProfileImage.objects.filter()
form = AddImage()


def base(request):
    if request.user.id != None:
        profile = get_object_or_404(Profile, id=request.user.id)
    else:
        profile = ""
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():

            form = form.save(commit=False)
            form.profile = request.user.profile
            form.save()
            return redirect(base)
    else:
        form = AddImage()
    return render(request, "allcontent.html", {"users": users,
                                         "images": images,
                                         "profile": profile,
                                         "form": form})

def user(request, user_id):
    profille = get_object_or_404(Profile, id=user_id)
    if request.user.id != None:
        profile = get_object_or_404(Profile, id=request.user.id)
    else:
        profile = ""
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():

            form = form.save(commit=False)
            form.profile = request.user.profile
            form.save()
            return redirect(userpage)
    else:
        form = AddImage()
    return render(request, "user.html", {"profile": profile,
                                         "profille": profille,
                                         "form": form})
# def user(request, user_id):
#     profile = get_object_or_404(Profile, id=1)
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#
#     print(request.session.session_key)
#     return render(request, 'user.html', {"profile": profile})


def search_users(request):
    return render_to_response('search.html', {"users": users})


def search(request):
    query = request.GET.get('q')
    if query != "":
        founded_users = User.objects.filter(Q(username__icontains=query))
    else:
        founded_users = ''
    #founded_profiles = ''
    #for founded_user in founded_users:

    return render(request, "user.html", {'founded_users': founded_users})
