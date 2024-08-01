from django.shortcuts import render, redirect, reverse
from .models import Curso, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        usuario = request.user
        if usuario.is_authenticated:
            return redirect('curso:homecursos')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return  reverse('curso:login')
        else:
            return reverse('curso:criarconta')

# def homecursos(request):
#     context = {}
#     lista_cursos = Curso.objects.all()
#     context['lista_cursos'] = lista_cursos
#     return render(request, "homecursos.html", context)

class Homecursos(LoginRequiredMixin, ListView):
    template_name = "homecursos.html"
    model = Curso

class Detalhecurso(LoginRequiredMixin, DetailView):
    template_name = "detalhecurso.html"
    model = Curso

    def get(self, request, *args, **kwargs ):
        curso = self.get_object()
        curso.visualizacoes += 1
        curso.save()
        usuario = request.user
        usuario.aulas_assistidas.add(curso)
        return super().get(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhecurso, self).get_context_data(**kwargs)
        cursos_relacionados = Curso.objects.filter(categoria=self.get_object().categoria)
        context["cursos_relacionados"] = cursos_relacionados
        return context

class Pesquisarcurso(LoginRequiredMixin, ListView):
    template_name = "pesquisar.html"
    model = Curso

    def get_queryset(self):
        param_query = self.request.GET.get('query')
        if param_query:
            object_list = self.model.objects.filter(titulo__icontains=param_query)
            return object_list
        else:
            return None

class Editarperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return  reverse('curso:homecursos')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('curso:login')

#@login_required
# def logout(request):
#     return render(request, "logout.html",{})


