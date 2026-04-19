from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: ## to change plural name in admin panel. if not added, it shows 'Entrys' not 'Entries'
        verbose_name_plural = "entries" #custom plural name
    def __str__(self):
        """Return a string representation of the model."""
        if (len(self.text) <= 70):
            return self.text
        return f"{self.text[:70]}..."  # Return first 50 characters of the entry, it shows in admin panel to identify entries    