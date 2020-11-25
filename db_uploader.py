import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "o9o9.settings")
django.setup()

from user.models    import User
from product.models import Product, Brand, ProductGroup, MainCategory, SubCategory, SubSubCategory
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
        order_number    = row[1]
        order_date      = row[2]
        name            = row[3]
        address         = row[4]
        phone_number    = row[5]
        description     = row[6]
        order_status_id = row[7]

        Order.objects.create(
            user_id=user_id,
            order_number=order_number, 
            order_date=order_date, 
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
        productgroup_id = row[10]
        maincategory_id = row[11]
        subcategory_id = row[12]
        subsubcategory_id = row[13]

        Product.objects.create(
            name=name,
            brand_id=brand_id,
            price=price,
            more_information=more_information,
            seller_information=seller_information,
            exchange=exchange,
            thumbnail_image=thumbnail_image,
            detail_image=detail_image,
            essential=essential,
            optional=optional,
            productgroup_id=productgroup_id,
            maincategory_id=maincategory_id,
            subcategory_id=subcategory_id,
            subsubcategory_id=subsubcategory_id
            )

# OrderItem

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
        user_id          = row[0]
        product_id       = row[1]
        title            = row[2]
        content          = row[3]
        question_type_id = row[4]
        answer_status_id = row[5]
        created_at       = row[6]
        
        Question.objects.create(user_id=user_id, product_id=product_id, title=title, content=content, question_type_id=question_type_id, answer_status_id=answer_status_id, created_at=created_at)

'''
# WatchList

CSV_PATH_PRODUCTS = './WatchList.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        user_id = row[0]
        product_id = row[1]
        
        WatchList.objects.create(user_id=user_id, product_id=product_id)

# CheckId

CSV_PATH_PRODUCTS = './CheckId.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        checkid = row[0]
        
        CheckId.objects.create(checkid=checkid)
'''