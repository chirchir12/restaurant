from django.db import models
from django.db.models.signals import pre_save
from restaurant.utils import upload_image_to, unique_slug_generator


class Menu(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.FileField(upload_to=upload_image_to)

    def __str__(self):
        return self.title


def menu_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(menu_pre_save_receiver, sender=Menu)
