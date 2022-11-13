from django.contrib import admin

from .models import Question, Choice, Pessoa, Parentesco, Dependente

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

class DependenteInline(admin.TabularInline):
    model = Dependente 
    extra = 3
    fk_name = "titular"

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo')
    inlines = [DependenteInline]
    search_fields = ['nome']
    list_filter = ['sexo']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Parentesco)

