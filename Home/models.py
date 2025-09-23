from django.db import models

#makemigrations = create changes and store it in a file
#migrate = apply the pending changes created by makemigrations 

#create your models here
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    datetime = models.DateTimeField()  # Automatically set the datetime on creation

    def __str__(self):
        return self.name
