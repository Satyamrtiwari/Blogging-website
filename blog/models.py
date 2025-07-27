from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to=)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)


    def __str__(self):
        return self.title

     
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=500)

    date = models.DateField()

    def __str__(self):
        return self.name

