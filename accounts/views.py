from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, LoginForm


@csrf_protect
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #user.active = False
        if user is not None:
            # Is the account active? It could have been disabled.
            # user.is_active = False
            if user.is_active:
                login(request, user)
                return render(request, 'accounts_2/index.html')
                #return HttpResponseRedirect("/profile/")
            else:
                return HttpResponse("You have to Wait for admin approval.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'pass_admin_approval_wrong.html')
    else:
        return render(request, 'login.html', context)


@csrf_protect
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return render(request, 'register_success.html')
    return render(request, 'accounts/registration.html', context)


@login_required
def profile(request):
    #if request.user.update:
        #request.user.save()
    args = {"user": request.user }

    return render(request, 'accounts_2/index.html', args)







@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')










def login(request):
    return render(request, 'accounts/login.html')


def registration(request):
    return render(request, 'accounts/registration.html')
