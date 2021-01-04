from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now().replace(tzinfo=None)
        return now - datetime.timedelta(days=1) <= datetime.datetime.strptime(str(self.pub_date), '%Y-%m-%d') <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


if __name__ == '__main__':
    print(type(timezone.now()))
    print(datetime.timedelta(days=1))
    print(type(datetime.timedelta(days=1)))
