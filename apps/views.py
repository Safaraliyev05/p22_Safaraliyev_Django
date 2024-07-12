from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.forms import UserRegisterModelForm
from apps.models import Product
from apps.tasks import send_to_email


class RegisterCreateView(CreateView):
    template_name = 'apps/register.html'
    form_class = UserRegisterModelForm
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save()
        send_to_email.delay('Saytimizga xush kelibsiz', form.data['email'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.all()


