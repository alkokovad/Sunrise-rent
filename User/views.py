from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import django.contrib.auth.views as admin_views
from User.forms import SignUpForm


class SignUpView(View):
    template_name = 'User/auth/sign_up.html'

    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect(reverse_lazy('mainpage'))
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('mainpage'))
        return super().dispatch(request, *args, **kwargs)


class SignInView(admin_views.LoginView):
    template_name = 'User/auth/sign_in.html'

    def post(self, request):
        return redirect(reverse_lazy('mainpage'))

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('mainpage'))
        return super().dispatch(request, *args, **kwargs)
