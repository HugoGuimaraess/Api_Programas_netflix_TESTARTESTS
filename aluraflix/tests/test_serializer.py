from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer



class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em Latim',
            data_lancamento='2003-07-04',
            tipo='F',
            likes=240,
            deslikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_serializer(self):
        data = self.serializer.data
        self.assertEquals(set(data.keys()),set['titulo','data_lancamento','tipo','likes'])


    def test_valida_serializer(self):
        data = self.serializer.data
        self.assertEquals(data['titulo'],self.programa.titulo)
