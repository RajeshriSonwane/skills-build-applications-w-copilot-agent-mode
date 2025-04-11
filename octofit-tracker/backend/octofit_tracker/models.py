from djongo import models

class MinimalModel(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name