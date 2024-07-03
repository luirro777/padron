from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import (
    View,
    CreateView,
    TemplateView,
    ListView,
    DetailView
)

from django.views.generic.edit import (
    FormView
)

from .forms import LoginForm

from .models import User

from afiliados.models import Afiliado, Mesa

from .utils import render_to_pdf


class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:user-panel')
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class Panel(LoginRequiredMixin, TemplateView):
    template_name = "panel.html"
    login_url = reverse_lazy('users_app:user-login')

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = "lista-mesas.html"
    #paginate_by = 20
    #context_object_name: 'lista_mesas'

class MesaDetailView(LoginRequiredMixin, DetailView):
    model = Mesa
    template_name = "detalle-mesa.html"
    context_object_name = 'detalle'

class PadronMesaListView(LoginRequiredMixin, ListView):
    
    template_name = "padron_mesa.html"
    context_object_name = 'listado'
    #ordering = 'apellidos'

    def get_queryset(self):
        nro_mesa = self.kwargs['numero']        
        queryset = Afiliado.objects.filter(
            mesa__numero = nro_mesa
        ).order_by('apellidos')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(PadronMesaListView, self).get_context_data(**kwargs)
        context['numero'] = self.kwargs['numero']
        context['cant'] = Afiliado.objects.filter(
            mesa__numero = self.kwargs['numero']
        ).count()
        return context    

class PadronMesaListViewPdf(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        nro_mesa = self.kwargs['numero']           
        afiliados = Afiliado.objects.filter(
            mesa__numero = nro_mesa
        ).order_by('apellidos')
        cant = afiliados.count()
        data = {
            'listado' : afiliados,
            'numero' : nro_mesa,
            'cant' : cant
        }
        pdf = render_to_pdf('padron_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class PadronListView(LoginRequiredMixin, ListView):
    template_name = 'padron.html'
    paginate_by = 20
    ordering = 'apellidos'
    context_object_name = 'listado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Afiliado.objects.filter(
            apellidos__icontains=palabra_clave
        )
        return lista