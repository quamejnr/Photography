from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
import cloudinary


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.user.username} Profile"

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self, *args, **kwargs):
        # resizing images before saving
        super().save(*args, **kwargs)

        # with Image.open(self.image.path) as img:
        #     if (img.height or img.width) > 300:
        #         output_size = (300, 300)
        #         img.thumbnail(output_size)
        #         img.save(self.image.path)

        img = cloudinary.CloudinaryImage(self.image.path)
        img.build_url(width=100, height=100, crop="fill")
        img.image(width=100, height=100, crop="fill")
