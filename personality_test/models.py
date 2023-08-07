from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('neuroticism', 'Neuroticism'),
        ('extroversion', 'Extroversion'),
        ('openness', 'Openness'),
        ('agreeableness', 'Agreeableness'),
        ('conscientiousness', 'Conscientiousness'),
    )

    text = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    admin_only = models.BooleanField(default=False)  # New field to indicate if the category is admin-only

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"
