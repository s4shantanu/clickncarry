from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('ANDRA PRADESH','ANDRA PRADESH'),
    ('ARUNACHAL PRADESH','ARUNACHAL PRADESH'),
    ('ASSAM','ASSAM'),
    ('BIHAR','BIHAR'),
    ('CHANDIGARH','CHANDIGARH'),
    ('CHHATTISGARH','CHHATTISGARH'),
    ('DADRA & NAGAR HAVELI','DADRA & NAGAR HAVELI'),
    ('DAMAN & DIU','DAMAN & DIU'),
    ('DELHI','DELHI'),
    ('GOA','GOA'),
    ('GUJARAT','GUJARAT'),
    ('HARYANA','HARYANA'),
    ('HIMACHAL PRADESH','HIMACHAL PRADESH'),
    ('JAMMU & KASHMIR','JAMMU & KASHMIR'),
    ('JHARKHAND','JHARKHAND'),
    ('KARNATAKA','KARNATAKA'),
    ('KERALA','KERALA'),
    ('LAKSHADWEEP','LAKSHADWEEP'),
    ('MADHYA PRADESH','MADHYA PRADESH'),
    ('MAHARASHTRA','MAHARASHTRA'),
    ('MANIPUR','MANIPUR'),
    ('MEGHALAYA','MEGHALAYA'),
    ('MIZORAM','MIZORAM'),
    ('NAGALAND','NAGALAND'),
    ('ODISHA','ODISHA'),
    ('PUDUCHERRY','PUDUCHERRY'),
    ('PUNJAB','PUNJAB'),
    ('RAJASTHAN','RAJASTHAN'),
    ('SIKKIM','SIKKIM'),
    ('TAMIL NADU','TAMIL NADU'),
    ('TELANGANA','TELANGANA'),
    ('TRIPURA','TRIPURA'),
    ('UTTAR PRADESH','UTTAR PRADESH'),
    ('UTTARAKHAND','UTTARAKHAND'),
    ('WEST BENGAL','WEST BENGAL'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(default=0)
    ip = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return str(self.id)

    
    


# Create your models here.