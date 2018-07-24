from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

class Person(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField(default=18)
	slug = models.CharField(max_length=30, blank=True, null=True)

	# class Meta:
	# 	ordering = ['-name']

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("app:detail", kwargs={"slug": self.slug })

def slug_pre_save(sender, instance, *args, **kwargs):
	print(instance)
	if not instance.slug and instance.name :
		instance.slug = slugify(instance.name)

pre_save.connect(slug_pre_save, sender=Person)
