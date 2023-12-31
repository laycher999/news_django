from django_filters import FilterSet, CharFilter, DateRangeFilter
from .models import Post


class ProductFilter(FilterSet):
    create_time = DateRangeFilter()

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'name': ['icontains'],
           'author__username': ['icontains'],
       }