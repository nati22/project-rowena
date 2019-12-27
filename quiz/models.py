from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
