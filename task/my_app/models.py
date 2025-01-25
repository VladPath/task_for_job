from django.db import models

# Create your models here.

class Patient(models.Model):
    
    # дата рождения
    date_of_birth = models.DateField()
    # массив строк с названиями диагнозов
    diagnoses = models.ManyToManyField('DiagnosesArr', blank=True, related_name='tags')
    # дата создания записи
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.diagnoses
    
class DiagnosesArr(models.Model):
    diagnose = models.CharField(max_length=100, db_index=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.diagnose