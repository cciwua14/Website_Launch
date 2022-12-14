from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    phone_no = PhoneNumberField(blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    join_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['join_date']

    def __str__(self):
        return f'{self.email}'
