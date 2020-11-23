from django.views   import View
from django.http    import JsonResponse

from .models        import MainCategory, Product, ProductGroup

class CategoryView(View):
    def get(self, request):
        categories = MainCategory.objects.all()
        category_list = [{
            "id"   : category.id,
            "name" : category.name
        } for category in categories]

        return JsonResponse({"category": category_list}, status=200)

class ProductListView(View):
    def get(self, request, maincategory_id):
        group_products = ProductGroup.objects.prefetch_related('product_set')
        nongroup_products = Product.objects.select_related('maincategory', 'subcategory').filter(maincategory=maincategory_id, essential=False)

        product_list = []
        nonproduct_list = []

        for group_product in group_products:
            if not group_product.product_set.all().first():
                continue
            if not group_product.product_set.all().first().maincategory_id == maincategory_id:
                continue
            product_list.append({
                "id"             : group_product.product_set.all().first().id,
                "imageUrl"       : group_product.product_set.all().first().thumbnail_image,
                "title"          : group_product.name,
                "price"          : group_product.product_set.all().first().price,
                "brand"          : group_product.product_set.all().first().brand.name
                # "watchlist": product.watch_product.count(),
                # "buy_count": product.buy_product.count(),
            })

        for nongroup_product in nongroup_products:
            nonproduct_list.append({
                "id" : nongroup_product.id,
                "imageUrl" : nongroup_product.thumbnail_image,
                "title" : nongroup_product.name,
                "price" : nongroup_product.price,
                "brand" : nongroup_product.brand.name
                # "watchlist": product.watch_product.count(),
                # "buy_count": product.buy_product.count(),
            })

        products = product_list + nonproduct_list

        return JsonResponse({'productList': products}, status=200)

class SubCategoryView(View):
    def get(self, request, maincategory_id, subcategory_id):
        group_products = ProductGroup.objects.prefetch_related('product_set')
        nongroup_products = Product.objects.select_related('maincategory', 'subcategory').filter(maincategory=maincategory_id, subcategory=subcategory_id, essential=False)

        product_list = []
        nonproduct_list = []

        for group_product in group_products:
            if not group_product.product_set.all().first():
                continue
            if group_product.product_set.all().first().subcategory_id != subcategory_id:
                continue
            product_list.append({
                "id"             : group_product.product_set.all().first().id,
                "imageUrl"       : group_product.product_set.all().first().thumbnail_image,
                "title"          : group_product.name,
                "price"          : group_product.product_set.all().first().price,
                "brand"          : group_product.product_set.all().first().brand.name
                # "watchlist": product.watch_product.count(),
                # "buy_count": product.buy_product.count(),
            })

        for nongroup_product in nongroup_products:
            nonproduct_list.append({
                "id" : nongroup_product.id,
                "imageUrl" : nongroup_product.thumbnail_image,
                "title" : nongroup_product.name,
                "price" : nongroup_product.price,
                "brand" : nongroup_product.brand.name
                # "watchlist": product.watch_product.count(),
                # "buy_count": product.buy_product.count(),
            })

        products = product_list + nonproduct_list

        return JsonResponse({'productList': products}, status=200)