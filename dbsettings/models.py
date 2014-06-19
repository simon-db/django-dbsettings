from django.db import models
from django.contrib.sites.models import Site
from django.db.models.signals import  post_save
from django.dispatch import receiver
class SettingManager(models.Manager):
    def get_query_set(self):
        all = super(SettingManager, self).get_query_set()
        return all.filter(site=Site.objects.get_current())

class Setting(models.Model):
    site = models.ForeignKey(Site)
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True)
    attribute_name = models.CharField(max_length=255)
    value = models.TextField(blank=True)

    objects = SettingManager()

    def __nonzero__(self):
        return self.id is not None

    def save(self):
        self.site = Site.objects.get_current()
        return super(Setting, self).save()


@receiver(post_save)
def clear_cache(sender, **kwargs):
    from django.core.cache import cache
    if sender == SettingManager or sender == Setting:
        try:
            cache.clear()
        except:
            pass