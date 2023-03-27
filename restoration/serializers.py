from rest_framework import serializers
from .models import CEO, Recipe, Restaurant, Chef

class CEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEO
        fields = ["first_name", "last_name", "email"]

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ["first_name", "last_name"]

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["recipe_name", "recipe_type", "chef"]

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["business_name", "recipes", "headmaster"]