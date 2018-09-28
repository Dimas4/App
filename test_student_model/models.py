from django.db import models

work_type = (
    ('В', 'Вопрос'),
    ('С', 'Самостоятельная работа'),
    ('К', 'Контрольная работа'),
)


class Lesson(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.text[:10]


class Work(models.Model):
    description = models.TextField()
    type = models.CharField(max_length=50, choices=work_type)
    question = models.ManyToManyField(Question)
