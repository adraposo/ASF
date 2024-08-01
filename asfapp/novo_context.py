from .models import Curso

def lista_curso_recente(request):
    lista_cursos = Curso.objects.all().order_by('-data_criacao')[0:6]
    if lista_cursos:
        curso_destaque = lista_cursos[0]
    else:
        curso_destaque = None
    return {"lista_curso_recente" : lista_cursos, "curso_destaque" : curso_destaque}


def lista_curso_emalta(request):
    lista_cursos = Curso.objects.all().order_by('-visualizacoes')
    return {"lista_curso_emalta" : lista_cursos}