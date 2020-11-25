import json

from django.views   import View
from django.http    import JsonResponse

from .models        import MainCategory, Product, ProductGroup
from user.models    import User
from order.models   import Order, OrderStatus, OrderItem

class CategoriesView(View):
    def get(self, request):
        categories = [{
            "id"   : category.id,
            "name" : category.name
        } for category in MainCategory.objects.all()]

        return JsonResponse({"categories": categories}, status=200)

class ProductsView(View):
    def get(self, request):
        main_category_id = request.GET.get('main')
        sub_category_id = request.GET.get('sub')

        if main_category_id:
            group_products = ProductGroup.objects.prefetch_related('product_set')
            nongroup_products = Product.objects.select_related('brand').filter(maincategory=int(main_category_id), essential=False)

            product_list = []
            nonproduct_list = []

            for group_product in group_products:
                if not group_product.product_set.all().first():
                    continue
                if group_product.product_set.all().first().maincategory_id != int(main_category_id):
                    continue
                product_list.append({
                    "id"             : group_product.product_set.all().first().id,
                    "imageUrl"       : group_product.product_set.all().first().thumbnail_image,
                    "title"          : group_product.name,
                    "price"          : group_product.product_set.all().first().price,
                    "brand"          : group_product.product_set.all().first().brand.name,
                    "watchlist"      : group_product.product_set.all().first().watchlist.count(),
                    "buy_count"      : group_product.product_set.all().first().buy_count.count()
                })

            for nongroup_product in nongroup_products:
                nonproduct_list.append({
                    "id"       : nongroup_product.id,
                    "imageUrl" : nongroup_product.thumbnail_image,
                    "title"    : nongroup_product.name,
                    "price"    : nongroup_product.price,
                    "brand"    : nongroup_product.brand.name,
                    "watchlist": nongroup_product.watchlist.count(),
                    "buy_count": nongroup_product.buy_count.count()
                })

            products = product_list + nonproduct_list

            return JsonResponse({'productList': products}, status=200)

        if sub_category_id:
            group_products = ProductGroup.objects.prefetch_related('product_set')
            nongroup_products = Product.objects.select_related('brand').filter(subcategory=int(sub_category_id), essential=False)

            product_list = []
            nonproduct_list = []

            for group_product in group_products:
                if not group_product.product_set.all().first():
                    continue
                if not group_product.product_set.all().first().subcategory_id == int(sub_category_id):
                    continue
                product_list.append({
                    "id"        : group_product.product_set.all().first().id,
                    "imageUrl"  : group_product.product_set.all().first().thumbnail_image,
                    "title"     : group_product.name,
                    "price"     : group_product.product_set.all().first().price,
                    "brand"     : group_product.product_set.all().first().brand.name,
                    "watchlist" : group_product.product_set.all().first().watchlist.count(),
                    "buy_count" : group_product.product_set.all().first().buy_count.count()
                })

            for nongroup_product in nongroup_products:
                nonproduct_list.append({
                    "id": nongroup_product.id,
                    "imageUrl": nongroup_product.thumbnail_image,
                    "title": nongroup_product.name,
                    "price": nongroup_product.price,
                    "brand": nongroup_product.brand.name,
                    "watchlist": nongroup_product.watchlist.count(),
                    "buy_count": nongroup_product.buy_count.count()
                })

            products = product_list + nonproduct_list

            return JsonResponse({'productList': products}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        product = Product.objects.select_related('maincategory', 'subcategory', 'brand', 'productgroup').get(id=product_id)
        product_detail = {
            "maincategoryId"    : product.maincategory.id,
            "subcategoryId"     : product.subcategory.id,
            "imageUrl"          : product.thumbnail_image,
            "detailproductImage": product.detail_image,
            "title"             : product.name,
            "price"             : product.price,
            "brand"             : product.brand.name,
            "productgroup"      : product.productgroup.name if product.essential else '',
            "moreInformation"   : {
                "tax_status"              : product.more_information.tax_status,
                "receipt"                 : product.more_information.receipt,
                "business_classification" : product.more_information.business_classification,
                "producer_importer"       : product.more_information.producer_importer,
                "origin"                  : product.more_information.origin,
                "manufacturing_date"      : product.more_information.manufacturing_date,
                "shelf_life"              : product.more_information.shelf_life,
                "storage_method"          : product.more_information.storage_method,
                "delivery_period"         : product.more_information.delivery_period
            },
            "sellerInformation" : {
                "representative"  : product.seller_information.representative,
                "business_number" : product.seller_information.business_number,
                "phone_number"    : product.seller_information.phone_number,
                "email"           : product.seller_information.email
            },
            "exchange"          : {
                "return_shipping_fee" : product.exchange.return_shipping_fee,
                "where_to_send"       : product.exchange.where_to_send,
                "detail_information"  : product.exchange.detail_information
            }
        }

        return JsonResponse({'product': product_detail}, status=200)

class WatchListView(View):
    # @check_user
    def post(self, request):
        data = json.loads(request.body)
        user_id = 3

        if not user_id:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        if 'product_id' not in data:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        if not Product.objects.filter(id=data['product_id']).exists():
            return JsonResponse({'message': 'POST_NOT_FOUND'}, status=404)



        user_model = User.objects.get(id=user_id)
        product_model = Product.objects.filter(id=data['product_id'])
        product_model.watchlist.add(user_model)
        return JsonResponse({'message': 'SUCCESS'}, status=200)

    # @check_user
    def delete(self, request):
        data = json.loads(request.body)
        user_id = 3

        user_model = User.objects.get(id=user_id)
        product_model = Product.objects.get(id=data['product_id'])
        product_model.watchlist.remove(user_model)
        return JsonResponse({'message': 'SUCCESS'}, status=200)