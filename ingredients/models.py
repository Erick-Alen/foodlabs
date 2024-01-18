from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=31)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="ingredients")
    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.name}>"
