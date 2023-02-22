from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Face(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    face_image = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    face = models.ForeignKey(Face, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name