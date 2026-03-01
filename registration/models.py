from django.db import models
from django.contrib.auth.models import User


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='participant')
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    school = models.CharField(max_length=200, verbose_name="Учебное заведение")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.school}"
