from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import PostInfo
from Post import forms


# Create your views here.

def post_list(request):
    list_display = PostInfo.objects.all()
    return render(request, 'post/post_list.html', {"list_display": list_display})


def post_detail(request, pk):
    detail_display = PostInfo.objects.get(id=pk)
    return render(request, 'post/post_details.html', {'detail_display': detail_display})


def post_create(request):
    if request.method == 'POST':
        form = forms.PostInfoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('post:list')

    else:
        form = forms.PostInfoForm
        context = {"form": form}
        return render(request, 'post/post_create.html', context)
