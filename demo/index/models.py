from django.db import models

# Create your models here.
class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.category_id},{self.name}"