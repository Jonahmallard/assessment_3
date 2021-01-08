from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.WidgetCreate.as_view(), name='add_widget'),
    path('delete/<int:widget_id>/', views.delete_widget, name='delete_widget'),
    path('widgets/<int:widget_id>/add_widget/', views.add_widget, name='add_widget')
]