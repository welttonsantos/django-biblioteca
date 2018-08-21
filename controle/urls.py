from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns =[
    path('',views.index, name='index'),
    path('criar_clientes/',views.criar_clientes, name='clientes'),
    path('criar_funcionario/',views.criar_funcionario, name='funcionario'),
    path('criar_livro/',views.criar_livro, name='livros'),

    path('busca_cliente/',views.busca_cliente, name='busca_cliente'),
    path('busca_funcionario/',views.busca_funcionario, name='busca_funcionario'),
    path('busca_livro/',views.busca_livro, name='busca_livro'),

    path('controle/cliente/<int:cliente_id>/',views.update_cliente, name='update_cliente'),
    path('controle/funcionario/<int:funcionario_id>/',views.update_funcionario, name='update_funcionario'),
    path('controle/livro/<int:livro_id>/',views.update_livro, name='update_livro'),

    path('delete/cliente/<int:cliente_id>/',views.delete_cliente, name='delete_cliente'),
    path('delete/funcionario/<int:funcionario_id>/',views.delete_funcionario, name='delete_funcionario'),
    path('delete/livro/<int:livro_id>/',views.delete_livro, name='delete_livro'),

    path('processo/',views.processo, name='processo'),
    path('busca_processo/',views.busca_processo, name ='busca_processo')
    #path('update_processo/<int:processo_id>/',views.update_processo, name ='update_processo')





]
