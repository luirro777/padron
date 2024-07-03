from django.views.generic import (
    View,
    CreateView,
    TemplateView,
    ListView
)
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from .models import Afiliado, Mesa
from .forms import AfiliadoForm
from django.shortcuts import redirect



class InitialView(View):
    form_class = AfiliadoForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():                        
            nro_dni = form.cleaned_data['dni']
            detalle = Afiliado.objects.filter(                
                dni = nro_dni 
            )
            return render(request,'detalle.html',{'detalle':detalle})
        return render(request, self.template_name, {'form': form})


