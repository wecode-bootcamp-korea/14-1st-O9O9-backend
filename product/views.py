from .models import Product
from product.models import Product
import json
from django.views import View
from django.http import request,JsonResponse
from django.db.models import Q

class ProductSearch(View):
    def get(self,request):
        data = json.loads(request.body)

        products = Product.objects.filter(Q(name__icontains = data['product_name'])|Q(brand__name__icontains = data['product_name']))

        product_list = [
            {
                'name' : product.name,
                'brand': product.brand.name,
            }for product in products
        ]
        return JsonResponse({'message':product_list},status=200)
