from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio


class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')

    def test_datos_laboratorio(self):
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio 1')
        self.assertEqual(laboratorio.nombre, 'Laboratorio 1')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'País 1')


class InicioTests(TestCase):
    def test_laboratorios_url_responde_200(self):
        url = '/laboratorio/mostrar/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #reverse
    def test_laboratorio_url_responde_200(self):
        url = reverse('lista_laboratorios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Listado de Laboratorios")
        self.assertNotContains(response, "No es la Página") 