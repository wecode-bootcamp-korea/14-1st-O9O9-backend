import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "o9o9.settings")
django.setup()

from user.models    import User
from product.models import Product, Brand, ProductGroup, MainCategory, SubCategory, SubSubCategory, MoreInformation, SellerInformation, Exchange
from order.models   import OrderItem, Order, OrderStatus, Shipment
from review.models  import PhotoReview, Review, Question, QuestionType, AnswerStatus

# User

CSV_PATH_PRODUCTS = './User.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        username_id   = row[0]
        password      = row[1]
        name          = row[2]
        phone_number  = row[3]
        email_address = row[4]

        User.objects.create(
            username_id=username_id,
            password=password,
            name=name,
            phone_number=phone_number,
            email_address=email_address
            )

# OrderStatus

CSV_PATH_PRODUCTS = './OrderStatus.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        status = row[0]

        OrderStatus.objects.create(status=status)

# Order

CSV_PATH_PRODUCTS = './Order.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        user_id         = row[0]
        order_date      = row[1]
        order_number    = row[2]
        name            = row[3]
        address         = row[4]
        phone_number    = row[5]
        description     = row[6]
        order_status_id = row[7]

        Order.objects.create(
            user_id=user_id,
            order_date=order_date,
            order_number=order_number,
            name=name,
            address=address,
            phone_number=phone_number,
            description=description,
            order_status_id=order_status_id
            )

# Shipment

CSV_PATH_PRODUCTS = './Shipment.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        company_name = row[0]
        tracking_number = row[1]

        Shipment.objects.create(company_name=company_name, tracking_number=tracking_number)

# Brand

CSV_PATH_PRODUCTS = './Brand.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]

        Brand.objects.create(name=name)

# ProductGroup

CSV_PATH_PRODUCTS = './ProductGroup.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]

        ProductGroup.objects.create(name=name)

# MainCategory

CSV_PATH_PRODUCTS = './MainCategory.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]

        MainCategory.objects.create(name=name)

# SubCategory

CSV_PATH_PRODUCTS = './SubCategory.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]

        SubCategory.objects.create(name=name)

# SubSubCategory

CSV_PATH_PRODUCTS = './SubSubCategory.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]

        SubSubCategory.objects.create(name=name)

# WatchList

# CSV_PATH_PRODUCTS = './WatchList.csv'
#
# with open(CSV_PATH_PRODUCTS) as in_file:
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         user_id = row[0]
#         product_id = row[1]
#
#         WatchList.objects.create(user_id=user_id, product_id=product_id)

# Product

CSV_PATH_PRODUCTS = './Product.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        name = row[0]
        brand_id = row[1]
        price = row[2]
        more_information = row[3]
        seller_information = row[4]
        exchange = row[5]
        thumbnail_image = row[6]
        detail_image = row[7]
        essential = row[8]
        optional = row[9]
        productgroup = row[10]
        maincategory_id = row[11]
        subcategory_id = row[12]
        subsubcategory_id = row[13]

        Product.objects.create(
            name=name,
            brand_id=brand_id,
            price=price,
            more_information_id=more_information,
            seller_information_id=seller_information,
            exchange_id=exchange,
            thumbnail_image=thumbnail_image,
            detail_image=detail_image,
            essential=True if essential == "TRUE" else False,
            optional=True if optional == "TRUE" else False,
            productgroup_id=productgroup,
            maincategory_id=maincategory_id,
            subcategory_id=subcategory_id,
            subsubcategory_id=subsubcategory_id
            )

OrderItem

CSV_PATH_PRODUCTS = './OrderItem.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        product_id  = row[0]
        order_id    = row[1]
        quantity    = row[2]
        shipment_id = row[3]
        
        OrderItem.objects.create(product_id=product_id, order_id=order_id, quantity=quantity, shipment_id=shipment_id)

# Review

CSV_PATH_PRODUCTS = './Review.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        user_id      = row[0]
        product_id   = row[1]
        satisfaction = row[2]
        content      = row[3]
        created_at   = row[4]
        
        Review.objects.create(user_id=user_id, product_id=product_id, satisfaction=satisfaction, content=content, created_at=created_at)

# Question

CSV_PATH_PRODUCTS = './Question.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        user_id       = row[0]
        product_id    = row[1]
        content       = row[2]
        question_type  = row[3]
        answer_status = row[4]
        created_at    = row[5]
        
        Question.objects.create(user_id=user_id, product_id=product_id, content=content, question_type_id=question_type, answer_status_id=answer_status, created_at=created_at)

# MoreInformation

CSV_PATH_PRODUCTS = './MoreInformation.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        tax_status         = row[0]
        receipt      = row[1]
        business_classification    = row[2]
        producer_importer            = row[3]
        origin         = row[4]
        manufacturing_date    = row[5]
        shelf_life     = row[6]
        storage_method = row[7]
        delivery_period = row[8]

        MoreInformation.objects.create(
            tax_status=tax_status,
            receipt=receipt,
            business_classification=business_classification,
            producer_importer=producer_importer,
            origin=origin,
            manufacturing_date=manufacturing_date,
            shelf_life=shelf_life,
            storage_method=storage_method,
            delivery_period=delivery_period
            )

# SellerInformation

CSV_PATH_PRODUCTS = './SellerInformation.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        representative         = row[0]
        business_number      = row[1]
        phone_number    = row[2]
        email            = row[3]

        SellerInformation.objects.create(
            representative=representative,
            business_number=business_number,
            phone_number=phone_number,
            email=email
            )

# Exchange

CSV_PATH_PRODUCTS = './Exchange.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        return_shipping_fee         = row[0]
        where_to_send      = row[1]
        detail_information    = row[2]


        Exchange.objects.create(
            return_shipping_fee=return_shipping_fee,
            where_to_send=where_to_send,
            detail_information=detail_information
            )

# QuestionType

CSV_PATH_PRODUCTS = './QuestionType.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        question_type = row[0]

        QuestionType.objects.create(question_type=question_type)

# AnswerStatus

CSV_PATH_PRODUCTS = './AnswerStatus.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        answer_status = row[0]

        AnswerStatus.objects.create(answer_status=answer_status)


