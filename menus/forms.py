
from django import forms

from picky_menu_picker import RestauarantLocation
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user = None, *args, **kwargs):
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestauarantLocation.objects.none() #.exclude(item__isnull = False)
