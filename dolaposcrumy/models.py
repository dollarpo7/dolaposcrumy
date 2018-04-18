from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class ScrumyUser(models.Model):
    userName = models.EmailField(max_length=70, blank=True, null=False)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.userName

#New Model
class ScrumyStatus(models.Model):
    STATUS = (
        ('WT', 'Weekly Task'),
        ('DT', 'Daily Task'),
        ('V', 'Verified'),
        ('D', 'Done'),
    )
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.status


class ScrumyGoals(models.Model):
    user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    status_id = models.ForeignKey(ScrumyStatus, on_delete=models.CASCADE) #New field
    task = models.TextField()

    def get_absolute_url(self):
        return reverse('dolaposcrumy:home')

    def __str__(self):
        return self.task



