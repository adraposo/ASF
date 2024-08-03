
from django.urls import path, reverse_lazy, re_path                                       #re_path acrecentada para retirar problema debug = fase
from .views import Homepage, Homecursos, Detalhecurso, Pesquisarcurso, Editarperfil, Criarconta
from django.conf import settings                                                          #linha acrecentada para retirar problema debug = fase
from django.contrib.auth import views as auth_view
from django.views.static import serve                                                     #linha acrecentada para retirar problema debug = fase

from django.contrib import admin                                                          #linha acrecentada para retirar problema debug = fase
from django.conf.urls.static import static                                                #linha acrecentada para retirar problema debug = fase
from django.contrib.staticfiles.urls import staticfiles_urlpatterns                       # #linha acrecentada para retirar problema debug = fasenew


app_name = 'curso'

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),      #linha acrecentada para retirar problema debug = fase
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),    #linha acrecentada para retirar problema debug = fase
    path('', Homepage.as_view(), name='homepage'),
    path('cursos/', Homecursos.as_view(), name='homecursos'),
    path('cursos/<int:pk>', Detalhecurso.as_view(), name='detalhecurso'),
    path('pesquisa/', Pesquisarcurso.as_view(), name='pesquisarcurso'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
   # path('logout/', logout, name='logout' ),
    path('editarperfil/<int:pk>', Editarperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('curso:homecursos')), name='mudarsenha'),
]