from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced, ReviewRating #, ProductGallery

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']

# @admin.register(ReviewRating)
# class ReviewRatingModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'product', 'subject', 'review', 'rating', 'status']

# admin.site.register(ProductGallery)
# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(OrderPlaced)
# admin.site.register(ReviewRating)
#admin username: admin
#password: Pass@123

