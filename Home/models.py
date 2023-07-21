from django.db import models

'''
we are using the sqlite3 database which is already connected with this projects
check settings
'''
# Create your models here.
class Students(models.Model):

    class Meta:
        verbose_name_plural = "Students"

    name = models.CharField(max_length=100)
    section = models.CharField(max_length=20)
    phone_no = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name