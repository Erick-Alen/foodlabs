from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.street} {self.city}, {self.state} {self.zip_code}>"
