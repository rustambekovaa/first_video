from django.db import models
from django.urls import reverse



class Women(models.Model):
    title = models.CharField(max_length = 255,verbose_name = 'Заголовок')
    content = models.TextField(blank = True,verbose_name = 'Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",verbose_name = 'Фото')
    time_create = models.DateTimeField(auto_now_add = True,verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now = True,verbose_name = 'Время изменения')
    is_published = models.BooleanField(default = True,verbose_name = 'Запущен ли ')
    cat = models.ForeignKey('Category', on_delete = models.PROTECT,null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name  = "Известные женшины"
        verbose_name_plural =  "Известные женшины"
        ordering = ['-time_create','title']

class Category (models.Model):
    name = models.CharField(max_length = 100, db_index = True,verbose_name = 'Катергория')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_id':self.pk})
    
    class Meta:
        verbose_name  = "Катергория"
        verbose_name_plural =  "Катергории"
        ordering = ['id']
# Create your models here.
