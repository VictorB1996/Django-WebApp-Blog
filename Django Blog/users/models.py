from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # If the user is deleted, also delete the profile
    image = models.ImageField(default = "default.jpg", upload_to = "profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        profile_image = Image.open(self.image.path)
        
        if profile_image.height > 300 or profile_image.width > 300:
            output_image_size = (300, 300)
            profile_image.thumbnail(output_image_size)
            profile_image.save(self.image.path)



