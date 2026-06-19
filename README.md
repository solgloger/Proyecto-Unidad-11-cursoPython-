# Biblioteca Django
Sistema de gestión de libros desarrollado con Django. Permite listar, buscar, crear, editar y eliminar libros, con control de acceso según roles de usuario.

--

## Requisitos
- Python 3.10+
- pip

---

## Instalación y configuración

### 1. Clonar o descomprimir el proyecto
```bash
cd "Unidad 11 Libreria"
```
### 2. Crear y activar el entorno virtual
```bash
python -m venv .venv
```
En Windows:
```bash
.venv\Scripts\activate
```
En Mac/Linux:
```bash
source .venv/bin/activate
```
### 3. Instalar dependencias
```bash
pip install django
```
### 4. Configurar la base de datos
```bash
python manage.py migrate
```
### 5. Crear un superusuario
```bash
python manage.py createsuperuser
```
### 6. Iniciar el servidor
```bash
python manage.py runserver
```
Accedé a la app en: http://127.0.0.1:8000

---

## Carga de datos de ejemplo
Desde el panel de administración (`/admin/`) podés crear:
1. **Autores** — nombre y email
2. **Categorías** — nombre
3. **Libros** — título, autor, categoría, fecha de publicación y disponibilidad

---
## Funcionalidades

### Listado y búsqueda
- Accedé a `/libros/` para ver todos los libros disponibles.
- Usá el buscador para filtrar por título, autor o categoría.

### Detalle de libro
- Hacé click en "Ver" en cualquier libro para ver su información completa.

### Crear, editar y eliminar
- Solo disponible para usuarios con el grupo **Bibliotecario**.
- Los botones de acción solo aparecen si el usuario tiene el permiso correspondiente.

---

## Grupos y permisos
Desde el admin (`/admin/`) configurar los siguientes grupos:

| Grupo         | Permisos |
|---            |---       |
| Bibliotecario | Agregar, editar, eliminar y ver libros |
| Usuario       | Solo ver libros |

Para asignar un grupo a un usuario: **Admin → Usuarios → seleccionar usuario → Grupos**.

