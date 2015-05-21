from django.conf.urls import patterns, url

from blastplus import views

urlpatterns = patterns('',

                       url(r'^blastn/', views.blastn),
                       url(r'^tblastn/', views.tblastn),
                       url(r'^blast/$', views.blastn),
                       url(r'^blastp/$', views.blastp),
                       url(r'^blastx/$', views.blastx),

                       )
