from django.db import models

from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Discussion(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="static/images/", blank=True, null=True)
    hashtags = models.JSONField()  # List of hashtags
    created_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    discussion = models.ForeignKey(
        Discussion, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Discussion, null=True, blank=True, on_delete=models.CASCADE
    )  # Discussion or Comment
    comment = models.ForeignKey(
        Comment, null=True, blank=True, on_delete=models.CASCADE
    )
