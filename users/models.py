from django.db import models


class User(models.Model):
    # class meta replaces users = User.objects.all().order_by("id") into models
    class Meta:
        ordering = ("id")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    # auto_now_add - automatically set the field to now when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now - automatically set the field to now every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first_name} {self.last_name}>"
