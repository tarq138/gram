from django.shortcuts import render, get_object_or_404, redirect
from .models import  ProfileImage
from .forms import AddImage


def userpage(request):
    #users = Profile.objects.all()
    images = ProfileImage.objects.filter()
    form = AddImage()
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = request.user
            form.save()
            return redirect(userpage)
    else:
        form = AddImage()
    return render(request, "user.html", {#"users" : users,
                                         "images": images,
                                         "form" : form})
