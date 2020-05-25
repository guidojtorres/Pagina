from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()


class Producto(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    precio = models.FloatField()
    stock = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    imagen = models.ImageField()
    slug = models.SlugField(blank=True, null=True)
    talles = models.CharField(max_length=3)
    categoria = models.CharField(choices=[('C', 'Carteras'), ('Z', 'Zapatos'), ('J', 'Jeans'), (
        'ZA', 'Zapatillas'), ('V', 'Vestidos'), ('A', 'Accesorios'), ('B', 'Botas')], max_length=15, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True, max_length=256)
    imagen2 = models.ImageField(blank=True, null=True)
    imagen3 = models.ImageField(blank=True, null=True)
    imagen4 = models.ImageField(blank=True, null=True)
    imagen5 = models.ImageField(blank=True, null=True)
    caracteristica1 = models.CharField(blank=True, null=True, max_length=30)
    caracteristica2 = models.CharField(blank=True, null=True, max_length=30)
    caracteristica3 = models.CharField(blank=True, null=True, max_length=30)
    caracteristica4 = models.CharField(blank=True, null=True, max_length=30)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("productos:producto_detail", kwargs={"slug": self.slug})
