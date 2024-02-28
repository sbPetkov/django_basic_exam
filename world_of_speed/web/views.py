from django.shortcuts import render

from world_of_speed.help_funcs.help_funcs import get_profile


def index(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'web/index_no_profile.html')

    context = {
        'profile': profile
    }
    return render(request, 'web/index_with_profile.html', context)
