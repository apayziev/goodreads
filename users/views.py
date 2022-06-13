from django.shortcuts import redirect, render
from django.views import View
from users.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import UpdateView
# Create your views here.


class RegisterView(View):
    def get(self, request):

        create_form = UserCreateForm()

        context = {
            'register_form': create_form
        }

        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()

            # create user account
            return redirect('users:login')

        else:
            context = {
                'register_form': create_form
            }

            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')

            return redirect('books:books_list')
        else:
            return render(request, 'users/login.html', {'login_form': login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out')
        return redirect('landing_page')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {'user': request.user})


# class ProfileUpdateView(LoginRequiredMixin, View):
#     def get(self, request):
#         user_update_form = UserUpdateForm(instance=request.user)
#         return render(request, 'users/profile_update.html', {'form': user_update_form})

#     def post(self, request):
#         user_update_form = UserUpdateForm(
#             data=request.POST,
#             instance=request.user,
#             files=request.FILES
#         )
#         if user_update_form.is_valid():
#             user_update_form.save()
#             messages.success(request, 'Your profile has been updated')

#             return redirect('users:profile')
#         else:
#             return render(request, 'users/profile_update.html', {'form': user_update_form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_update.html'
    form_class = UserUpdateForm
    success_url = '/users/profile'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Your profile has not been updated')
        return super().form_invalid(form)

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
