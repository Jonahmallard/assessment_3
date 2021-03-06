from django.db import models
from django.urls import reverse
from django.forms import ModelForm

class Widget(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('index')

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = '__all__'