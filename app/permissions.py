from django.shortcuts import render

def user_required(function):
    def wrapper(request, *args, **kw):
        user = request.user

        if not user.is_authenticated:
            return render(request, 'blank.html', {})
        else:
            return function(request, *args, **kw)
    return wrapper