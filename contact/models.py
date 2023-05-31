from django.db import models
from django.utils import timezone

# Create your models here.
#id (primary key - automático)
#first_name (String), last_name (String), phone (String), email (email),
#created_date (date), description (text)

#category (foreign key), show (boolean), picture (image)

# owner (foreign key)

#"Tabela"
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

