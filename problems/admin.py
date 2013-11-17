from django.contrib import admin
from categories.admin import CategoryBaseAdmin

from problems.models import Problem, Choice, ConceptTag
from .models import ConceptTag

import logging
logger = logging.getLogger(__name__)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class ConceptTagAdmin(CategoryBaseAdmin):
    pass

class ConceptsFilter(admin.SimpleListFilter):
    title = 'Concepts'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'concept'

    def get_category_tree (category):
        """

        """
        categories = []
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        tuple = [ (c.slug, c.name) for c in ConceptTag.objects.all()]
        return tuple

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        slug = self.value()

        if slug:
                print 'slug = ', slug
                tag = ConceptTag.objects.get(slug=slug)
                subcategories_id = [tag.id for tag in tag.get_descendants(include_self=True)]
                queryset = queryset.filter(concepts__id__in=subcategories_id)

        return queryset

class ProblemAdmin(admin.ModelAdmin):
	# order the fields
	# fields = ['create_date', 'question']

	fieldsets = [
                (None, 				 {'fields':['question']}),
		('Date information', {'fields':['create_date'], 'classes':['collapse']}),
                ('Concepts', {'fields': ['concepts']})
	]

	inlines = [ChoiceInline]
	list_display = ('question', 'create_date', 'was_created_recently')
	list_filter = ['create_date', ConceptsFilter]
	search_fields = ['question']
	date_hierarchy = 'create_date'

admin.site.register(Problem, ProblemAdmin)
admin.site.register(ConceptTag, ConceptTagAdmin)