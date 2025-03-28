from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
   #path('admin/', admin.site.urls),
   path('',views.hello,name="hello"),
   path('about/',views.about ,name="about"),
   path('login/',views.login_user,name="login"),
   path('logout',views.logout_user,name="logout"),
   path('register/',views.register_user,name="register"),
   path('product/<int:pk>',views.product,name="product"),
    path('category/<str:foo>',views.category,name="category")
]