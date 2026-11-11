from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=150)
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True) # sarqvum a menak mi angam

    class Meta: # class-i configuracian
        ordering = ['-created_at'] # iranc hertakanutyuny ksksvi amenatarm lead-ov

    def __str__(self):
        return f'{self.name} ({self.contact})'
