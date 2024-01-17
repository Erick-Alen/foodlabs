from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    # blank is preferred for string fields
    description = models.TextField(blank=True)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.name}>"
