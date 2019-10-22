from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Cars(models.Model):
    make = models.CharField(max_length=200)
    year = models.IntegerField(default=1930)
    color = models.PositiveIntegerField(default=1, choices=(
        (1, 'red'), (2, 'blue'), (3, 'green')))

    def __str__(self):
        return self.make
