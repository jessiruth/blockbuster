from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_item, name='create'),
    path('show/xml/', views.show_xml, name='show_xml'),
    path('show/json/', views.show_json, name='show_json'),
    path('show/xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('show/json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('item/add/<int:id>/', views.add_amount, name='add_amount'),
    path('item/reduce/<int:id>/', views.reduce_amount, name='reduce_amount'),
    path('item/delete/<int:id>/', views.delete_item, name='delete_item'),
    path('get-item-json/', views.get_item_json, name='get_item_json'),
    path('create-ajax/', views.create_ajax, name='create_ajax'),
    path('delete-ajax/<int:id>/', views.delete_ajax, name='delete_ajax'),
    path('create-flutter/', views.create_flutter, name='create_flutter'),
]