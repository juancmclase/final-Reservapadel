from django.conf.urls import url

from . import views





urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #url(r'^books/$', views.BookListView.as_view(), name='books'),
    #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    #url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    #url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^quien/$', views.quien1, name='quien'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    #url(r'^club/$', views.clubes, name='clubes'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^añadirpistas/$', views.apistas, name='apistas'),
    url(r'^listaPistas/$', views.Pistalista.as_view(), name='pistalista'),
    url(r'^listaReservas/$', views.ReservaList.as_view(), name='reservalista'),
    url(r'^pista/(?P<pk>\d+)$', views.PistaDetailView.as_view(), name='pista-detail'),
    url(r'^reserva/(?P<pk>\d+)$', views.ReservasDetailView.as_view(), name='reserva-detail'),
    url(r'^reservas/$', views.re, name='reservas'),
    url(r'^listaContactos/$', views.Contactoslista.as_view(), name='contactolista'),
    url(r'^Contactos/(?P<pk>\d+)$', views.ContactosDetailView.as_view(), name='contacto-detail'),
    url(r'^EliminarReserva/$', views.eliminarreserva, name='eliminar-reserva'),
    url(r'^Perfil/$', views.UserprofileView.as_view(), name='perfil'),
    url(r'^password/$', views.PasswordsChangeView.as_view(template_name='password.html'), name='password'),
    url(r'^password_success/$', views.password_success, name='password_success'),
    url(r'^horario/$', views.hora, name='hora1'),
    url(r'^ajaxpista/$', views.load_pista, name='load_pista'),
    url(r'^ajaxhora/$', views.load_hora, name='load_hora'),
    
    
    
]
