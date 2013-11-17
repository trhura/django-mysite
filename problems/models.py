import datetime
from django.db import models
from django.utils import timezone

from categories.models import CategoryBase

class ConceptTag(CategoryBase):
    class Meta:
        verbose_name_plural = 'concept'

class Problem(models.Model):
        question = models.CharField(max_length=200)
        create_date = models.DateTimeField('date created')
        concepts = models.ManyToManyField(ConceptTag)

        def was_created_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.create_date < now

        was_created_recently.admin_order_field = 'create_date'
        was_created_recently.boolean = True
        was_created_recently.short_description = 'Created recently?'

        def __unicode__(self):
                return self.question

class Choice(models.Model):
        problem = models.ForeignKey(Problem)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

        def __unicode__(self):
                return self.choice_text
