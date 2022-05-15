from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from .models import Clients
from .filters import ClientsFilter
from .forms import ClientsForm

# -----------------------------------#
# Clients views
# -----------------------------------#


def clients_view(request):
    clients = Clients.objects.all().order_by('-id')
    filter = ClientsFilter(request.GET, queryset=clients)
    clients = filter.qs
    paginator = Paginator(clients, 25)
    page_number = request.GET.get('paginator')
    clients = paginator.get_page(page_number)
    context = {'clients': clients, 'filter': filter}
    return render(request, 'accounts/clients.html', context)

# -----------------------------------#
# Clients create view
# -----------------------------------#


class ClientsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/clients_form.html'
    form_class = ClientsForm
    success_url = '/accounts'
    success_message = 'client was created'
    error_message = 'client was not created'

# -----------------------------------#
# clients update view
# -----------------------------------#


class ClientsUpdateView(SuccessMessageMixin, UpdateView):
    model = Clients
    template_name = 'accounts/clients_form.html'
    form_class = ClientsForm
    success_url = '/accounts'
    success_message = 'client was updated'
    error_message = 'client was not updated'


# -----------------------------------#
# clients delete view
# -----------------------------------#

class ClientsDeleteView(SuccessMessageMixin, DeleteView):
    model = Clients
    template_name = 'accounts/clients_delete.html'
    success_url = '/accounts'
    success_message = 'client was deleted'
    error_message = 'client was not deleted'

    # -----------------------------------#
    # login view
    # -----------------------------------#


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('clients')
        else:

            render(request, 'accounts/login.html',
                   {'error': 'username or password is incorrect'})
    return render(request, 'accounts/login.html')
