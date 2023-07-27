from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile


# Create your views here.


def profile_list_view(request):
    #profiles = Profile.objects.all()
     profiles = Profile.objects.exclude(user=request.user)
     return render(request, 'profile/UserProfileList.html', {"profiles": profiles})


#def profile_list_view_non_signup_signin(request):
   # non_signup_signin_profiles = Profile.objects.all()
    #return render(request, 'profile/nonSigninSignupUserProfileList.html',
                  #{"non_signup_signin_profiles": non_signup_signin_profiles})


def profile_not_own_view(request, slug):
    notOwnProfile = Profile.objects.get(slug=slug)
    #context = {
    #    'notOwnProfile': notOwnProfile
    #}

    if request.method == "POST":
        current_user_profile = request.user.profile

        action = request.POST['follow']

        if action == "unfollow":
            current_user_profile.follows.remove(notOwnProfile)
        elif action == "follow":
            current_user_profile.follows.add(notOwnProfile)

        current_user_profile.save()
    return render(request, 'profile/notOwnProfile.html', {"notOwnProfile": notOwnProfile})
