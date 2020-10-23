from django.db import models #from e Import: Agregar algo de otros archivos
from django.utils import timezone

#class es una palabra clave que indica que estamos definiendo un objeto.
#Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.

class Post(models.Model): #define nuestro modelo con sus propiedades
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#es una relación (link) con otro modelo.
    title = models.CharField(max_length=200) #defines un texto con un número limitado de caracteres.
    text = models.TextField() #para texto largo sin límite.
    created_date = models.DateTimeField(
            default=timezone.now) #Fecha y hora
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #La regla de nomenclatura es utilizar minúsculas y guiones bajos en lugar de espacios
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #Lo que regresa la funcion