from django.urls import path

from blastplus.views import blastn, tblastn, blastn, blastp, blastx

urlpatterns = [
    path('blastn', blastn, name='blastn'),
    path('tblastn', tblastn, name='tblastn'),
    path('blast', blastn, name='blastn'),
    path('blastp', blastp, name='blastp'),
    path('blastx', blastx, name='blastx'),

]
