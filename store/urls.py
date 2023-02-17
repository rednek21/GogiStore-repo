from django.urls import path

from .views import index, all_electronics, product_info, about, delivery_info, guarantee, trade_in, regularcustomers, \
    contacts

app_name = 'store'

urlpatterns = [
    path('all_electronics/', all_electronics, name='all_electronics'),
    path('all-electronics/category_id:<int:category_id>', all_electronics, name='categories'),
    path('all-electronics/brand_id:<int:brand_id>', all_electronics, name='brands'),
    path('product_info/product_id:<int:product_id>', product_info, name='product_info'),
    path('about/', about, name='about'),
    path('delivery_info/', delivery_info, name='delivery_info'),
    path('guarantee/', guarantee, name='guarantee'),
    path('trade_in/', trade_in, name='trade_in'),
    path('regularcustomers/', regularcustomers, name='regularcustomers'),
    path('contacts/', contacts, name='contacts'),

]
