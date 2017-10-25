from django.db import models
from django.conf import settings
from picky_menu_picker.models import RestaurantLocation
from django.core.urlresolvers import reverse

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantLocation)
    # the items
    name = models.CharField(max_length = 120)
    contents = models.TextField(help_text= "separate by comma", max_length = 120)
    excludes = models.TextField(blank = True, null = True, help_text= "separate by comma", max_length = 120)
    public = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    
    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" 
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp'] # querysets ordered to recent, uses flipping + or -

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")