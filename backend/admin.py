from django.contrib import admin

from .models import Goat

class GoatAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['name']}),
		('Description', {'fields': ['description'], 'classes': ['collapse']}),
		('Score', {'fields': ['score']}),
		('Image', {'fields': ['image']}),
		('Number of Battles', {'fields': ['n_battles']}),
		('Number of Battles won', {'fields': ['wins']}),
		('Number of Battles lost', {'fields': ['lost']}),
		('Number of Battles draw', {'fields': ['draw']}),
	]

	search_fields = [
		'name',
	]

	readonly_fields = ('pub_date',)

	list_display = ('name',)

admin.site.register(Goat, GoatAdmin)