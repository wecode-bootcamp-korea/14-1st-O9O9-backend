import json
import uuid

from django.views     import View
from django.http      import JsonResponse

from user.models     import User
from product.models  import Product, Brand, ProductGroup, MainCategory, SubCategory, SubSubCategory
from .models         import OrderItem, Order, OrderStatus, Shipment

from user.utils import check_user

class OrderView(View):
    @check_user
    def post(self, request):
        data    = json.loads(request.body)
        user_id = request.user.id

        try:
            product_id = data['product_id']
            quantity   = data['quantity']
        
        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)
        
        order_status_id = 1
        order_number    = uuid.uuid4()

        products = OrderItem.objects.filter(product_id=product_id).select_related('order')
    
        if not products:
            Order.objects.create(
                user_id         = user_id,
                order_status_id = order_status_id,
                order_number    = order_number,
                )
            try:
                order = Order.objects.get(order_number=order_number)
            
            except Order.DoesNotExist:
                return JsonResponse({'message': "ORDER_NUMBER IS NOT EXIST"}, status = 401)

            except Order.MultipleObjectsReturned:
                return JsonResponse({'message': "ORDER_NUMBER IS DUPLICATED"}, status = 401)

            OrderItem.objects.create(
                product_id = product_id,
                quantity   = quantity,
                order_id   = order.id
                )
            
            return JsonResponse({'message': 'ITEM ADD IN CART'}, status=201)
            
        for product in products.all():
            if product.order.user_id == user_id and product.order.order_status_id == 1:
                product.quantity += quantity
                product.save()
                return JsonResponse({'message': 'ITEM ADD IN CART'}, status=201)
        
        Order.objects.create(
            user_id         = user_id,
            order_status_id = order_status_id,
            order_number    = order_number,
            )
        try:
            order = Order.objects.get(order_number=order_number)
        
        except Order.DoesNotExist:
            return JsonResponse({'message': "ORDER_NUMBER IS NOT EXIST"}, status = 401)

        OrderItem.objects.create(
            product_id = product_id,
            quantity   = quantity,
            order_id   = order.id
            )
        
        return JsonResponse({'message': 'ITEM ADD IN CART'}, status=201)

    @check_user
    def patch(self, request, product_id):
        data    = json.loads(request.body)
        user_id = request.user.id

        try:
            quantity        = data['quantity']
        
        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status = 400)

        products = OrderItem.objects.filter(product_id=product_id).select_related('order')

        for product in products.all():
            if product.order.user_id == user_id and product.order.order_status_id == 1:
                product.quantity = quantity
                product.save()

                return JsonResponse({'message': 'ITEM IS MODIFIED'}, status = 200)

    @check_user
    def get(self, request):
        user_id = request.user.id
        user_products = Order.objects.filter(user_id=user_id, order_status_id=1).prefetch_related('orderitem_set', 'orderitem_set__product').all().order_by('-id')

        return JsonResponse({
            'product' : [
            {
                'product_id'       : products.product.id,
                'name'             : products.product.name,
                'quantity'         : products.quantity,
                'price'            : products.product.price,
                'thumbnail_image'  : products.product.thumbnail_image,
            } 
            for user_product in user_products for products in user_product.orderitem_set.all()
        ]
        }, status = 200)

class OrderDeleteView(View):
    @check_user
    def post(self, request):
        data = json.loads(request.body)
        user_id = request.user.id
        
        try:
            product_ids = data['product_ids']

        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)

        for product_id in product_ids:
            products = OrderItem.objects.filter(product_id=product_id).select_related('order')
            
            for product in products.all():
                if product.order.user_id == user_id and product.order.order_status_id == 1:
                    product.delete()
        return JsonResponse({'message': 'ITEM IS DELETED'}, status = 200)