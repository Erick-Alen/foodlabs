from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first} {self.last_name}>"
