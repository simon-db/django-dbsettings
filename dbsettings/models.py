from django.db import models
from django.db.models.signals import  post_save
from django.dispatch import receiver

class Setting(models.Model):
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True)
    attribute_name = models.CharField(max_length=255)
    value = models.TextField(blank=True)

    def __nonzero__(self):
        return self.id is not None


@receiver(post_save)
def clear_cache(sender, **kwargs):
    from django.core.cache import cache
    if sender == Setting:
        try:
            cache.clear()
        except:
            pass
