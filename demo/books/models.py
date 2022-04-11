from django.db import models
from index.models import category

# Create your models here.
class books(models.Model):
    book_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"{self.book_id},{self.category_id},{self.name}"