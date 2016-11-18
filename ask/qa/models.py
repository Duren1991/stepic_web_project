from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Question(models.Model):
    objects = QuestionManager() 
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank=True,auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,default=1)
    likes = models.ManyToManyField(User, related_name='question', blank=True)
    #likes = models.TextField()
class QuestionManager(models.Manager):                                          
    def new(self):                                                              
	return self.order_by('added_at')
                                                          
    def popular():                                                          
        return self.order_by('rating') 
    '''def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})'''



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True,auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=1)
