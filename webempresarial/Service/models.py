from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)  # Debes especificar un número
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

    def __str__(self):
        return self.title