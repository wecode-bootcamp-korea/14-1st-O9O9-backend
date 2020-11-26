import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

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

        q = Q()
        if main_category_id:
            q &= Q(main_category_id=main_category_id)
        if sub_category_id:
            q &= Q(sub_category_id=sub_category_id)

        product_list = []
        nonproduct_list = []

        group_products = ProductGroup.objects.prefetch_related('product_set')
        nongroup_products = Product.objects.select_related(('brand').filter(q), essential = False)
        #
        # if Q(main_category_id) | Q(sub_category_id):
        #
        #     group_products = ProductGroup.objects.prefetch_related('product_set')
        #     # nongroup_products = Product.objects.select_related('brand').filter(Q(maincategory=main_category_id) | Q(subcategory=sub_category_id), essential=False)

            # product_list = []
            # nonproduct_list = []

        for group_product in group_products:
            if not group_product.product_set[0]:
                continue
            if group_product.product_set[0].maincategory_id != Q(main_category_id) | Q(sub_category_id):
                continue
            product_list.append({
                "id"             : group_product.product_set[0].id,
                "imageUrl"       : group_product.product_set[0].thumbnail_image,
                "title"          : group_product.name,
                "price"          : group_product.product_set[0].price,
                "brand"          : group_product.product_set[0].brand.name,
                "watchlist"      : group_product.product_set[0].watchlist.count(),
                "buy_count"      : group_product.product_set[0].buy_count.count()
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

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.select_related('maincategory',
                                                     'subcategory',
                                                     'brand',
                                                     'productgroup',
                                                     'more_information',
                                                     'seller_information',
                                                     'exchange'
                                                     ).get(id=product_id)

            product_detail = {
                "maincategory_id"     : product.maincategory.id,
                "subcategory_id"      : product.subcategory.id,
                "image_url"           : product.thumbnail_image,
                "detailproduct_image" : product.detail_image,
                "title"               : product.name if not product.essential else product.productgroup.name,
                "price"               : product.price,
                "brand"               : product.brand.name,
                "watchlist"           : product.watchlist.count() if not product.essential else ProductGroup.objects.get(id=product.productgroup.id).product_set.all()[0].watchlist.count(),
                "more_information"    : {
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
                "seller_information"  : {
                    "representative"  : product.seller_information.representative,
                    "business_number" : product.seller_information.business_number,
                    "phone_number"    : product.seller_information.phone_number,
                    "email"           : product.seller_information.email
                },
                "exchange"            : {
                    "return_shipping_fee" : product.exchange.return_shipping_fee,
                    "where_to_send"       : product.exchange.where_to_send,
                    "detail_information"  : product.exchange.detail_information
                }
            }

        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'NO_PRODUCT_FOUND'}, status=404)

        return JsonResponse({'product': product_detail}, status=200)

class WatchListView(View):
    pass
    # @check_user
    # def post(self, request):
    #     data = json.loads(request.body)
    #     user_id = request.user.id
    #
    #     user_model = User.objects.get(id=user_id)
    #     product_model = Product.objects.get(id=data['product_id'])
    #     if not product_model.essential:
    #         product_model.watchlist.add(user_model)
    #     else:
    #         ProductGroup.objects.get(id=product_model.productgroup.id).product_set.all()[0].watchlist.add(user_model)
    #
    #     return JsonResponse({'message': 'SUCCESS'}, status=200)
    #
    # @check_user
    # def delete(self, request):
    #     data = json.loads(request.body)
    #     user_id = request.user.id
    #
    #     user_model = User.objects.get(id=user_id)
    #     product_model = Product.objects.get(id=data['product_id'])
    #     if not product_model.essential:
    #         product_model.watchlist.add(user_model)
    #     else:
    #         ProductGroup.objects.get(id=product_model.productgroup.id).product_set.all()[0].watchlist.remove(user_model)
    #
    #     return JsonResponse({'message': 'SUCCESS'}, status=200)
