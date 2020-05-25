from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from Pagina.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random
from django.shortcuts import get_object_or_404
# Create your views here.


class IndexView(generic.ListView):
    model = models.Producto
    template_name = 'productos/index.html'


class ProductoDetailView(generic.DetailView):
    model = models.Producto
    template_name = 'productos/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(
            models.Producto, slug=self.kwargs.get('slug'))
        qs = models.Producto.objects.filter(
            categoria=product.categoria).exclude(slug=product.slug)
        context['related'] = qs
        return context


def contactoView(request):
    contacto = forms.ContactForm()
    if request.method == 'POST':
        contacto = forms.ContactForm(request.POST)
        subject = 'Dakota Store: Nuevo mensaje de ' + \
            str(contacto['nombre'].value())
        message = 'Dakota Store, ' + \
            str(contacto['nombre'].value()) + \
            ' se ha comunicado contigo.\n' + 'Email: ' + str(contacto['email'].value()) + '\nTelefono: ' + str(
                contacto['telefono'].value()) + '\nHorario preferente de llamada: ' + str(contacto['horario'].value()) + '\nComentarios adicionales: ' + str(contacto['comentarios'].value())
        recipient = EMAIL_HOST_USER
        send_mail(subject, message, EMAIL_HOST_USER, [recipient])
        return render(request, 'productos/contacto.html', {'mensaje': 'Tu contacto fue enviado con exito.', 'form': forms.ContactForm()})
    return render(request, 'productos/contacto.html', {'form': contacto})


class ProductList(generic.ListView):
    model = models.Producto
    template_name = 'productos/list.html'


class AgregarProducto(generic.CreateView):
    model = models.Producto
    template_name = 'productos/agregar.html'
    fields = ['nombre', 'precio', 'stock', 'color', 'imagen', 'talles', 'categoria', 'descripcion',
              'imagen2', 'imagen3', 'imagen4', 'imagen5', 'caracteristica1', 'caracteristica2', 'caracteristica3', 'caracteristica4']
