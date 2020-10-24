from django.urls import path
from . import views #Aquí estamos importando la función de Django path y todos nuestras views desde la aplicación blog (no tenemos una aun, pero veremos eso en un minuto!)

urlpatterns = [
    path('', views.post_list, name='post_list'),#Como puedes ver, estamos asociando una vista (view) llamada post_list a la URL raíz.
] #La última parte name='post_list' es el nombre de la URL que se utilizará para identificar a la vista.