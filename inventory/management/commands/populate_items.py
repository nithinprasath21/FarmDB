from django.core.management.base import BaseCommand
from inventory.models import Item

class Command(BaseCommand):
    help = 'Populate the database with predefined items'

    def handle(self, *args, **kwargs):
        items = [
            # Vegetables
            {'name': 'Tomato', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Potato', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Onion', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Carrot', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Brinjal', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Cabbage', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Cauliflower', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Spinach', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Green Peas', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Capsicum', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Radish', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Bitter Gourd', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Pumpkin', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Bottle Gourd', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Drumstick', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Sweet Potato', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Yardlong Bean', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Green Chilli', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Coriander', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Mint', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},
            {'name': 'Fenugreek', 'category': 'Vegetable', 'quantity': 0, 'storage_location': 'Godown'},

            # Fruits
            {'name': 'Apple', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Banana', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Mango', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Guava', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Papaya', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Pomegranate', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Orange', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Lemon', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Watermelon', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Chickoo', 'category': 'Fruit', 'quantity': 0, 'storage_location': 'Cold Storage'},

            # Liquids
            {'name': 'Milk', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Coconut Water', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Buttermilk', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Sugarcane Juice', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Fruit Juice', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Ice Cream', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Yogurt', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Vermicelli Kheer', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Pulses Milk', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
            {'name': 'Vegetable Soup', 'category': 'Liquid', 'quantity': 0, 'storage_location': 'Cold Storage'},
        ]

        for item in items:
            Item.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully populated items!'))
