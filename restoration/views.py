#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CEO, Recipe, Restaurant, Chef
from .serializers import CEOSerializer, RecipeSerializer, ChefSerializer, RestaurantSerializer

# Create your views here.

class CEOApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        #ceos = CEO.objects.filter(first_name = request.data.get('first_name'))
        ceos = CEO.objects.all()
        serializer = CEOSerializer(ceos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CEODetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, ceo_id):
        try:
            return CEO.objects.get(id = ceo_id)
        except CEO.DoesNotExist:
            return None

    def get(self, request, ceo_id, *args, **kwargs):
        ceo_instance = self.get_object(ceo_id)
        if not ceo_instance:
            return Response(
                {"res": "CEO with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CEOSerializer(ceo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CEOApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        ceos = CEO.objects.all()
        serializer = CEOSerializer(ceos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email')
        }
        serializer = CEOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CEODetailApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, ceo_id):
        try:
            return CEO.objects.get(id = ceo_id)
        except CEO.DoesNotExist:
            return None

    def get(self, request, ceo_id, *args, **kwargs):
        ceo_instance = self.get_object(ceo_id)
        if not ceo_instance:
            return Response(
                {"res": "CEO with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CEOSerializer(ceo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, ceo_id, *args, **kwargs):
        ceo_instance = self.get_object(ceo_id)
        if not ceo_instance:
            return Response(
                {"res": "CEO with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email')
        }
        serializer = CEOSerializer(instance=ceo_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ceo_id, *args, **kwargs):
        ceo_instance = self.get_object(ceo_id)
        if not ceo_instance:
            return Response(
                {"res": "CEO with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        ceo_instance.delete()
        return Response(
            {"res":"CEO deleted!"},
            status=status.HTTP_200_OK
        )


class RecipeApiView(APIView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecipeDetailApiView(APIView):
    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id = recipe_id)
        except Recipe.DoesNotExist:
            return None

    def get(self, request, recipe_id, *args, **kwargs):
        recipe_instance = self.get_object(recipe_id)
        if not recipe_instance:
            return Response(
                {"res": "Recipe with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RecipeSerializer(Recipe_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecipeApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'recipe_name': request.data.get('recipe_name'),
            'recipe_type': request.data.get('recipe_type'),
            'chef': request.data.get('chef')
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetailApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id = recipe_id)
        except Recipe.DoesNotExist:
            return None

    def get(self, request, recipe_id, *args, **kwargs):
        recipe_instance = self.get_object(recipe_id)
        if not recipe_instance:
            return Response(
                {"res": "Recipe with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RecipeSerializer(recipe_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, recipe_id, *args, **kwargs):
        recipe_instance = self.get_object(recipe_id)
        if not recipe_instance:
            return Response(
                {"res": "Recipe with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'recipe_name': request.data.get('recipe_name'),
            'recipe_type': request.data.get('recipe_type'),
            'chef': request.data.get('chef')
        }
        serializer = RecipeSerializer(instance=recipe_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, recipe_id, *args, **kwargs):
        recipe_instance = self.get_object(recipe_id)
        if not recipe_instance:
            return Response(
                {"res": "Recipe with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        recipe_instance.delete()
        return Response(
            {"res":"Recipe deleted!"},
            status=status.HTTP_200_OK
        )

class ChefApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        chefs = Chef.objects.all()
        serializer = ChefSerializer(chefs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
        }
        serializer = ChefSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChefDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, chef_id):
        try:
            return Chef.objects.get(id = chef_id)
        except Chef.DoesNotExist:
            return None

    def get(self, request, recipe_id, *args, **kwargs):
        chef_instance = self.get_object(chef_id)
        if not chef_instance:
            return Response(
                {"res": "Chef with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ChefSerializer(chef_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, chef_id, *args, **kwargs):
        chef_instance = self.get_object(chef_id)
        if not chef_instance:
            return Response(
                {"res": "Chef with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
        }
        serializer = ChefSerializer(instance=chef_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChefApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        chefs = Chef.objects.all()
        serializer = ChefSerializer(chefs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
        }
        serializer = ChefSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChefDetailApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, chef_id):
        try:
            return Chef.objects.get(id = chef_id)
        except Chef.DoesNotExist:
            return None

    def get(self, request, chef_id, *args, **kwargs):
        chef_instance = self.get_object(chef_id)
        if not chef_instance:
            return Response(
                {"res": "Chef with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ChefSerializer(chef_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, chef_id, *args, **kwargs):
        chef_instance = self.get_object(chef_id)
        if not chef_instance:
            return Response(
                {"res": "Chef with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
        }
        serializer = ChefSerializer(instance=chef_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, chef_id, *args, **kwargs):
        chef_instance = self.get_object(chef_id)
        if not chef_instance:
            return Response(
                {"res": "Chef with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        chef_instance.delete()
        return Response(
            {"res":"Chef deleted!"},
            status=status.HTTP_200_OK
        )


class RestaurantApiView(APIView):
    def get(self, request, *args, **kwargs):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestaurantDetailApiView(APIView):
    def get_object(self, restaurant_id):
        try:
            return Restaurant.objects.get(id = restaurant_id)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id)
        if not restaurant_instance:
            return Response(
                {"res": "Restaurant with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RestaurantSerializer(restaurant_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestaurantApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'business_name': request.data.get('business_name'),
            'recipes': request.data.get('recipes'),
            'headmaster': request.data.get('headmaster')
        }
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailApiAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, restaurant_id):
        try:
            return Restaurant.objects.get(id = restaurant_id)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id)
        if not restaurant_instance:
            return Response(
                {"res": "Restaurant with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RestaurantSerializer(restaurant_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id)
        if not restaurant_instance:
            return Response(
                {"res": "Restaurant with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'business_name': request.data.get('business_name'),
            'recipes': request.data.get('recipes'),
            'headmaster': request.data.get('headmaster')
        }
        serializer = RestaurantSerializer(instance=restaurant_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id, *args, **kwargs):
        restaurant_instance = self.get_object(restaurant_id)
        if not restaurant_instance:
            return Response(
                {"res": "Restaurant with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        restaurant_instance.delete()
        return Response(
            {"res":"Restaurant deleted!"},
            status=status.HTTP_200_OK
        )