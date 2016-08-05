from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class CourseManager(models.Manager):

    def highlined(self):
        return self.filter(is_highline=True)


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')
    category = models.ForeignKey(Category, verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    is_highline = models.BooleanField('Destaque', default=True, blank=True)
    price = models.DecimalField(
        'Preço', default=0, decimal_places=2, max_digits=8
    )
    objects = CourseManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name