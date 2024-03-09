from rest_framework.views import APIView, status, Request, Response
from .models import Recipe
from .serializers import RecipeSerializer
from ingredients.models import Ingredient


class RecipeView(APIView):
    def post(self, req: Request) -> Response:
        serializer = RecipeSerializer(data=req.data)
        # if not serializer.is_valid():
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        ingredients = serializer.validated_data.pop("ingredients")
        recipe = Recipe.objects.create(**serializer.validated_data)

        # get the ingredient list

        for ingredient_item in ingredients:
            try:
                # django field lookup => iexact
                ingredient = Ingredient.objects.get(name__iexact=ingredient_item["name"])
            except Ingredient.DoesNotExist:
                ingredient = Ingredient.objects.create(**ingredient_item)
            recipe.ingredients.add(ingredient)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # def get(self, req: Request) -> Response:
        # recipes = recipe.objects.filter(ingredients__name__iexact)
