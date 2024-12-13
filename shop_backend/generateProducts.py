import os
import django
from faker import Faker
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_backend.settings')
django.setup()

from shop.models import Product

# Initialize Faker
faker = Faker()

def generate_products(n=50):
    for _ in range(n):
        name = faker.word().capitalize()
        description = faker.text(max_nb_chars=200)
        price = round(random.uniform(10.0, 1000.0), 2)
        discount_percentage = round(random.uniform(0.0, 50.0), 2)
        rating = round(random.uniform(0.0, 5.0), 2)
        stock = random.randint(0, 500)
        brand = faker.company() if random.choice([True, False]) else None
        category = random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Toys'])
        thumbnail = None  # Update to valid image path if needed
        images = None     # Update to valid image paths if needed

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            discount_percentage=discount_percentage,
            rating=rating,
            stock=stock,
            brand=brand,
            category=category,
            thumbnail=thumbnail,
            images=images,
        )

# Generate 50 products
generate_products(50)
