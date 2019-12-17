from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Goat

import random

# Create your views here.
def index(request):
	voted = False
	number_of_goats = Goat.objects.all().count()
	if number_of_goats < 2:
		return HttpResponseRedirect(reverse('backend:add_goat'))

	g1 = Goat.get_random()
	g2 = Goat.get_random()

	while g1.pk == g2.pk:
		g2 = Goat.get_random()

	winner = None
	loser = None

	if request.COOKIES:
		won_id = request.COOKIES.get('won')
		los_id = request.COOKIES.get('los')

		if won_id:
			won_id = int(won_id)
		if los_id:
			los_id = int(los_id)

		winner = get_object_or_404(Goat, pk=won_id)
		loser = get_object_or_404(Goat, pk=los_id)

		winner.n_battles += 1
		winner.wins += 1
		winner.score += 1. / winner.n_battles
		winner.save()

		loser.n_battles += 1
		loser.lost += 1
		loser.score -= 1. / loser.n_battles
		loser.save()
		voted = True

	context = {'goat1': g1, 'goat2': g2, 'voted': voted, 'winner': winner, 'loser': loser}
	return render(request, 'backend/index.html', context)

class GoatDetailView(generic.DetailView):
	model = Goat
	template_name = 'backend/goat_detail.html'


"""
def vote(request, winner_id, loser_id):
	winner = get_object_or_404(Goat, pk=winner_id)
	winner.n_battles += 1
	winner.wins += 1
	winner.score += 1. / winner.n_battles
	winner.save()

	loser = get_object_or_404(Goat, pk=loser_id)
	loser.n_battles += 1
	loser.lost += 1
	loser.score -= 1. / loser.n_battles
	loser.save()
	return HttpResponseRedirect(reverse('backend:index'))
"""
