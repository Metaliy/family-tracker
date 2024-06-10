from django.db import models

from api.accounts.models import CustomUser


class Task(models.Model): 
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    durations = models.DecimalField(max_digits=5, decimal_places=1)
    place = models.CharField(max_length=100)
    creator = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE)  # Добавьте это поле

    
    class Meta:
        app_label = 'quickstart'
  
    def __str__(self):
        return self.name

