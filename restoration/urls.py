from django.urls import path, include
from .views import (
    CEOApiView, CEODetailApiView, CEOApiAdminView, CEODetailApiAdminView,
    RecipeApiView, RecipeDetailApiView, RecipeApiAdminView, RecipeDetailApiAdminView,
    RestaurantApiView, RestaurantDetailApiView, RestaurantApiAdminView, RestaurantDetailApiAdminView,
    ChefApiView, ChefDetailApiView, ChefApiAdminView, ChefDetailApiAdminView,
)

urlpatterns = [
    path('api/ceo/', CEOApiView.as_view()),
    path('api/ceo/<int:ceo_id>/', CEODetailApiView.as_view()),
    path('api/recipe/', RecipeApiView.as_view()),
    path('api/recipe/<int:recipe_id>', RecipeDetailApiView.as_view()),
    path('api/restaurant/', RestaurantApiView.as_view()),
    path('api/restaurant/<int:restaurant_id>', RestaurantDetailApiView.as_view()),
    path('api/chef/', ChefApiView.as_view()),
    path('api/chef/<int:chef_id>', ChefDetailApiView.as_view()),
    path('api/admin/ceo/', CEOApiAdminView.as_view()),
    path('api/admin/ceo/<int:ceo_id>/', CEODetailApiAdminView.as_view()),
    path('api/admin/recipe/', RecipeApiAdminView.as_view()),
    path('api/admin/recipe/<int:recipe_id>', RecipeDetailApiAdminView.as_view()),
    path('api/admin/restaurant/', RestaurantApiAdminView.as_view()),
    path('api/admin/restaurant/<int:restaurant_id>', RestaurantDetailApiAdminView.as_view()),
    path('api/admin/chef/', ChefApiAdminView.as_view()),
    path('api/admin/chef/<int:chef_id>', ChefDetailApiAdminView.as_view()),
]