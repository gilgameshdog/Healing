from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _

class Categoria(models.Model): 
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria',max_length= 100, null= False, blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    id = models.AutoField(primary_key= True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    title = models.CharField('Titulo' ,max_length=200, blank= False, null= False)
    slug = models.CharField('Slug', max_length=100, blank= False, null= False)
    descripcion = models.CharField('Descripcion', max_length=100, blank= False, null= False)
    text = RichTextField('Contenido')
    imagen = models.ImageField('imagen', upload_to='imagenes/',null=True)
    created_date = models.DateTimeField('Fecha de creacion',
            default=timezone.now)
    published_date = models.DateTimeField('Fecha de Publicacion',
            default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
        permissions = (
            ('profesor',_('Es profesor')),
            ('alumno',_('Es alumno')),
        )


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Formulario(models.Model):
    nombre = models.CharField('Nombre ',max_length= 100)
    apellidos = models.CharField('Apellido ',max_length= 150)
    correo = models.EmailField('Correo Electronico', max_length= 200)
    asunto = models.CharField('Asunto', max_length= 100)
    mensaje = models.TextField('Mensaje')