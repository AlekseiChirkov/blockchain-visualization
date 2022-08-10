from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    """Post model to create posts"""

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.title}"
