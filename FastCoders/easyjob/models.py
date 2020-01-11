from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=20)
    phoneno = models.IntegerField(10)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=20)
    document = models.FileField(upload_to='profiles/pdfs/')

    def __str__(self):
        return self.first_name






