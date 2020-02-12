from django.contrib import admin
from .models import Question, Sold_Product
# Register your models here.


class RadiusAdmin(admin.ModelAdmin):

    list_display = ["product", "date_of_purchase", "Qty", "purchase_price", "sale_price", "category"]
    list_display_links = ["product", "date_of_purchase"]
    list_filter = ["category"]
    search_fields = ["product"]


admin.site.register(Question, RadiusAdmin)
admin.site.register(Sold_Product)