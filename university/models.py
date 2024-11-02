from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Введите имя')
    last_name = models.CharField(max_length=50, verbose_name='Введите фамилию')
    age = models.IntegerField(verbose_name='Введите возраст')
    student_id = models.IntegerField(verbose_name='Введите номер студ.билета', default=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} - {self.first_name}'
