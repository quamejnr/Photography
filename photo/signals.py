from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Post
import cloudinary


@receiver(pre_delete, sender=Post)
def picture_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
