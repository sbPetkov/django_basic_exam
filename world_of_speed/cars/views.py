from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic

from world_of_speed.cars.models import Car
from world_of_speed.help_funcs.help_funcs import get_profile


class ReadOnlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

        return form


class CarCreateView(generic.CreateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image', 'price')
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()

        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["image"].widget.attrs["placeholder"] = "https://..."

        return form


class CarListview(generic.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'


class CarDetailView(generic.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'


class CarEditView(generic.UpdateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image', 'price')
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(ReadOnlyViewMixin, generic.DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(Car, fields=('type', 'model', 'year', 'image', 'price'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
