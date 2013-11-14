from django.contrib import admin
from problems.models import Problem, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class ProblemAdmin(admin.ModelAdmin):
	# order the fields
	# fields = ['create_date', 'question']

	fieldsets = [
		(None, 				 {'fields':['question']}),
		('Date information', {'fields':['create_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'create_date', 'was_created_recently')
	list_filter = ['create_date']
	search_fields = ['question']
	date_hierarchy = 'create_date'

admin.site.register(Problem, ProblemAdmin)
