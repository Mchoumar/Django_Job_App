from django.db import models


# Table model for the user data
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # Similar to the initialization instance, but it automatically prints a string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
