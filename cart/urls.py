from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.cart_summary,name="cart_summary"),
    path('add/<int:product_id>/', views.add_cart,name="add_to_cart"),
    path('remove/<int:product_id>/', views.remove_cart,name="remove_cart"),
    #path('clear/', views.clear_cart,name="clear_cart"),
    path('update/<int:product_id>/', views.update_cart,name="update_cart")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
