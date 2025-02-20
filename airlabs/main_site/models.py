from django.db import models

class Testimonials(models.Model):
    """
    This data model is to create a table for testimonials.
    """
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
