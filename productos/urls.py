from django.urls import path
from . import views
app_name = 'productos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('producto/<slug:slug>/',
         views.ProductoDetailView.as_view(), name='producto_detail'),
    path('contacto/', views.contactoView, name='contacto'),
    path('crear/', views.AgregarProducto.as_view(), name='crear'),
    path('productos/', views.ProductList.as_view(), name='list')
]
