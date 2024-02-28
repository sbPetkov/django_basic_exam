from django.urls import reverse_lazy
from django.views import generic

from world_of_speed.help_funcs.help_funcs import get_profile
from world_of_speed.profiles.forms import CreateProfileForm
from world_of_speed.profiles.models import Profile


class CreateProfileView(generic.CreateView):
    form_class = CreateProfileForm
    template_name = "profiles/profile-create.html"
    success_url = reverse_lazy('catalogue')


class DetailProfileView(generic.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cars_owned = get_profile().car_set.all()
        total_price = 0
        for car in cars_owned:
            total_price += car.price

        context['total_car_price'] = total_price
        return context


class EditProfileView(generic.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-edit.html"
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(generic.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()


