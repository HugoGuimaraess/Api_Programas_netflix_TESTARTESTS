from aluraflix.models import Programa
from django.test import TestCase


class FixtureTestCase(TestCase):
    fixtures=['programas_iniciais']



    def test_verifica_carregamento(self):
        programa_bizzaro= Programa.objects.get(pk=1)
        todos_os_programas= Programa.objects.all()
        self.assertEquals(programa_bizzaro.titulo,'Coisas Bizarras')
        self.assertEquals(len(todos_os_programas,),9)