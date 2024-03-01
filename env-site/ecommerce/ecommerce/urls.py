from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/',include("tags.urls")),
    path('authentication/',include("authentication.urls")),
    path('products/', include("products.urls")),
    path('orders_and_payments',include("orders_and_payments.urls")),
]