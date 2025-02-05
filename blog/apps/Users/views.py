from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from apps.Post.models import Noticia
from apps.Comentarios.models import Comentario
from .forms import RegistroForm, Formulario_Modificar_Usuario
from .models import CustomUser


def Ver_perfil(request, username):
    ctx = {}
    user = get_object_or_404(CustomUser, username=username)
    noticias_user = Noticia.objects.filter(usuario=user)
    comentarios_user = Comentario.objects.filter(usuario=user)
    ctx["noticias_user"] = noticias_user
    ctx["user"] = user
    ctx["comentarios_user"] = comentarios_user
    return render(request, "Users/profile.html", ctx)


class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("login")
    template_name = "Users/Acceso/registro.html"


class Modificar_usuario(UpdateView):
    model = CustomUser
    template_name = "Users/change_profile.html"
    form_class = Formulario_Modificar_Usuario

    def get_success_url(self):
        username = self.object.username
        return reverse_lazy("usuarios:ver_perfil", kwargs={"username": username})