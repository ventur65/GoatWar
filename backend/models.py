from django.db import models
from django.db.models import Max

import random
import datetime

def get_initial_score():
	queryset = Goat.objects.all()
	n_goats = queryset.count()
	if n_goats < 2:
		return 0
	return queryset.values_list('score', flat=True).order_by('score')[int(round(n_goats/2))]

def path_to_image(instance, filename):
	return '/'.join([instance.name, filename])

class Goat(models.Model):
	#user = models.ForeignKey(User)
	name = models.CharField(max_length=40)
	pub_date = models.DateField(auto_now_add = True)
	description = models.TextField(blank = True)
	_height = 100
	_width = 100
	# DA TOGLIERE BLANK = TRUE
	image = models.ImageField(upload_to = path_to_image,
							  height_field = '_height',
							  width_field = '_width',
							  null=False, blank = True)
	score = models.FloatField(default = get_initial_score)
	n_battles = models.IntegerField(default = 0)
	wins = models.IntegerField(default = 0)
	lost = models.IntegerField(default = 0)
	draw = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.name

	def get_random():
		max_id = Goat.objects.all().aggregate(max_id=Max("id"))['max_id']
		while True:
			pk = random.randint(1, max_id)
			goat = Goat.objects.filter(pk = pk).first()
			if goat:
				return goat