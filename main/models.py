from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Task nomi', max_length=200)
    hour = models.DateTimeField('Task vaqti', blank=True)
    complate = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Vazifa' 
        verbose_name_plural = 'Vazifalar' 