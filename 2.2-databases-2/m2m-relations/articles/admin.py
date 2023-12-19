from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_flags = []
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            main_flags.append(is_main)
        if main_flags.count(True) > 1:
            raise ValidationError('Только один тэг может быть основным')
        elif main_flags.count(True) == 0:
            raise ValidationError('Выберите основной тэг')
        elif main_flags[0] is not True:
            raise ValidationError('Основной тег обязательно указывается первым')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    fields = ['tag', 'is_main']
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass



