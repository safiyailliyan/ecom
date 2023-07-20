
from django.urls import path
from . import views
app_name='shop'
urlpatterns = [

    path('',views.allProducat,name='allProducat'),
    path('<slug:c_slug>/',views.allProducat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]