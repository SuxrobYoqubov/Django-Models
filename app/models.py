from django.db import models
from statistics import mode
from django.utils.html import format_html

# Create your models here.
jins = [
    ("Ayol","ayol"),
    ("Erkak","erkak")
]
class Talaba(models.Model):
    fio = models.CharField(max_length=500)
    birth = models.DateField(auto_now_add=False)
    phone = models.IntegerField()
    jinsi = models.CharField(max_length=300, choices=jins)
    image = models.ImageField(upload_to = 'pictures', default=False)
    file = models.FileField(upload_to="files", default=False)
    
    def show_image(self):
        return format_html(f'<img src = "{self.image.url}" height = "100" width = "100"/>')    
    
    def __str__(self):
        return self.fio