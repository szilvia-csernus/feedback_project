from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.user_name
