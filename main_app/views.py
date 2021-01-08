from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import CreateView
from .forms import WidgetForm

def index(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"

def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')

def add_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget_form = FeedingForm()
    return render(request, 'index.html', {
    # include the cat and feeding_form in the context
    'widget': widget, 'feeding_form': feeding_form
  })
# def add_widget(request, widget_id):
# 	# create the ModelForm using the data in request.POST
#   form = WidgetForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the widget_id assigned
#     new_widget = form.save(commit=False)
#     new_widget.widget_id = widget_id
#     new_widget.save()
#   return redirect('index', widget_id=widget_id)