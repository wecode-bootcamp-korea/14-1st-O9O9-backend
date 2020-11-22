import json

from django.views     import View
from django.http      import JsonResponse

from user.models     import User
from product.models  import Product, Brand, ProductGroup, MainCategory, SubCategory, SubSubCategory, WatchList
from .models         import OrderItem, Order, OrderStatus, Shipment, CartItem

from user.utils import check_user

class CartView(View):
    @check_user
    def post(self, request):
        data    = json.loads(request.body)

        try:
            product_id      = data['product_id']
            quantity        = data['quantity']
        
        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status = 400)
        
        exist_product = CartItem.objects.filter(product_id = product_id, user_id = user_id)
        
        if exist_product:
            product = CartItem.objects.get(product_id = product_id, user_id = user_id)
            product.quantity += quantity
            product.save()

            return JsonResponse({'message': 'ITEM ADD SUCCESS'}, status = 200)

        CartItem.objects.create(
            user_id     = user_id,
            product_id  = product_id,
            quantity    = quantity,
        )

        return JsonResponse({'message': 'ITEM ADD SUCCESS'}, status = 200)

    @check_user
    def get(self, request):
        user_id = request.user.id

        cart_items = CartItem.objects.filter(user_id=user_id).order_by('-id').values()
        
        try:
            return JsonResponse({
                'cart_item' : [
                {
                    'cart_id'          : cart_item['id'],
                    'product_name'     : Product.objects.get(id=cart_item['product_id']).name,
                    'quantity'         : cart_item['quantity'],
                    'price'            : Product.objects.get(id=cart_item['product_id']).price,
                    'thumbnail_image'  : Product.objects.get(id=cart_item['product_id']).thumbnail_image
                } 
                for cart_item in cart_items
            ]
            }, status = 200)

        except Exception as error_message:
            return JsonResponse({'message': error_message}, status = 400)