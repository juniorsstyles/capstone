from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    """
    Model representing a recipe.

    Attributes:
        name (CharField): The name of the recipe, limited to 200 characters.
        description (TextField): A detailed description of the recipe.
    """
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the recipe.

        Returns:
            str: The name of the recipe.
        """
        return self.name
