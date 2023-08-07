from django.contrib import admin
from django.db.models import QuerySet
from .models import Movie

# Register your models here.

class FilterRating(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('до 40', 'низкий'),
            ('от 40 до 59', 'средний'),
            ('от 60 до 79', 'высокий'),
            ('от 80', 'высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        rating = self.value()
        if rating == 'до 40':
            return queryset.filter(rating__lt=40)
        if rating == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=59)
        if rating == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=79)
        if rating == 'от 80':
            return queryset.filter(rating__gte=80)




@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'currency']
    ordering = ['-rating']
    list_per_page = 5
    actions = ['set_dollars', 'set_rubles']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', FilterRating]
    exclude = ['slug']


    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть'
        if movie.rating < 70:
            return 'Можно разок глянуть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'


    @admin.action(description='Перевести валюту в доллар')
    def set_dollars(self, requests, qs: QuerySet):
        count_change = qs.update(currency=Movie.USD)
        self.message_user(
            requests,
            f"Было обновлено {count_change} записей"
        )


    @admin.action(description='Перевести валюту в рубль')
    def set_rubles(self, requests, qs: QuerySet):
        count_change = qs.update(currency=Movie.RUB)
        self.message_user(
            requests,
            f"Было обновлено {count_change} записей"
        )