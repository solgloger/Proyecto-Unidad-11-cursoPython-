from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from .models import Autor, Categoria, Libro
from .forms import LibroForm
from datetime import date


class LibroFormTest(TestCase):

    def setUp(self):
        # Crea datos de prueba antes de cada test
        self.autor = Autor.objects.create(nombre="Gabriel García Márquez", email="gabo@email.com")
        self.categoria = Categoria.objects.create(nombre="Novela")

    def test_formulario_valido(self):
        # Verifica que el formulario es válido con datos correctos
        form = LibroForm(data={
            "titulo": "Cien años de soledad",
            "autor": self.autor.id,
            "categoria": self.categoria.id,
            "fecha_publicacion": "1967-05-30",
            "disponible": True,
        })
        self.assertTrue(form.is_valid())

    def test_formulario_sin_titulo(self):
        # Verifica que el formulario es inválido si falta el título
        form = LibroForm(data={
            "titulo": "",
            "autor": self.autor.id,
            "categoria": self.categoria.id,
            "fecha_publicacion": "1967-05-30",
            "disponible": True,
        })
        self.assertFalse(form.is_valid())


class LibroVistasTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.autor = Autor.objects.create(nombre="Gabriel García Márquez", email="gabo@email.com")
        self.categoria = Categoria.objects.create(nombre="Novela")
        self.libro = Libro.objects.create(
            titulo="Cien años de soledad",
            autor=self.autor,
            categoria=self.categoria,
            fecha_publicacion=date(1967, 5, 30),
            disponible=True,
        )
        # Usuario sin permisos
        self.lector = User.objects.create_user(username="lector", password="1234")

        # Usuario con permisos
        self.bibliotecario = User.objects.create_user(username="bibliotecario", password="1234")
        permiso = Permission.objects.get(codename="add_libro")
        self.bibliotecario.user_permissions.add(permiso)

    def test_lista_libros_accesible(self):
        # La lista de libros es pública
        response = self.client.get("/libros/")
        self.assertEqual(response.status_code, 200)

    def test_detalle_libro_accesible(self):
        # El detalle de un libro es público
        response = self.client.get(f"/libros/{self.libro.id}/")
        self.assertEqual(response.status_code, 200)

    def test_crear_libro_sin_permiso_redirige(self):
        # Un lector no puede acceder a crear libro
        self.client.login(username="lector", password="1234")
        response = self.client.get("/libros/crear/")
        self.assertEqual(response.status_code, 403)

    def test_crear_libro_con_permiso(self):
        # Un bibliotecario sí puede acceder a crear libro
        self.client.login(username="bibliotecario", password="1234")
        response = self.client.get("/libros/crear/")
        self.assertEqual(response.status_code, 200)

    def test_busqueda_por_titulo(self):
        # La búsqueda filtra correctamente por título
        response = self.client.get("/libros/?q=cien")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cien años de soledad")