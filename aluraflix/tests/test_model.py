from django.test import TestCase
from aluraflix.models import Programa


class ProgramaTestCase(TestCase):


    def teste_falha(self):
        self.fail('Test falhou')

    def setUp(self):
        self.programa=Programa(
            titulo='procurando ninguém em latim',
            data_lancamento='2003-07-04'
        )

    def teste_verifica_attrss_programa(self):
        self.assertEquals(self.programa.titulo,'procurando ninguém em latim')
        self.assertEquals(self.programa.tipo,'F')
        self.assertEquals(self.programa.likes,0)
        self.assertEquals(self.programa.data_lancamento,'2003-07-04')
        self.assertEquals(self.programa.dislikes,0)