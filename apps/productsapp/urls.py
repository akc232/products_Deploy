from django.conf.urls import url
from . import views

app_name='products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^destroy/(?P<id>\d+)$', views.delete, name='delete'),
]





# index: Display all products
# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product
