from django.contrib import admin #Para agregar, editar y borrar los posts que hemos modelado, usaremos el administrador (admin) de Django
from .models import Post

admin.site.register(Post)