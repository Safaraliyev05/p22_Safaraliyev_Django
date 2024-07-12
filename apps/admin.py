from django.contrib import admin

from apps.models import ProductImage, Product, ProductVideo


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 2
    min_num = 0


class ProductVideoStackedInline(admin.StackedInline):
    model = ProductVideo
    extra = 0
    max_num = 1
    min_num = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    inlines = [ProductImageStackedInline, ProductVideoStackedInline]


