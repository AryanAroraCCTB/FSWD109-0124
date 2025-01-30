
# /api/products
# GET /api/products?category=electronics&company=apple == # GET /api/products?company=apple&category=electronics
# GET /api/products?category=electronics
# GET /api/products?company=apple

# USING QUERY PARAMS
# GET /api/products
# QUERY: category, company, price-range, ratings, year

# USING PATH PARAMS
# GET /api/products
# GET /api/products/{company_name}
# GET /api/products/{category}
# GET /api/products/{company_name}/{category} != # GET /api/products/{category}/{company_name}

# ALL THE ORDER
# GET /orders
# POST /orders

# SPECIFIC
# GET /orders/{order_id}

# POST /orders 
# REQ BODY: { "name": "Product Name", "quantity": 5, "address": "123 Main St" }
# RES:      { "id": 123, "name": "Product Name", "quantity": 5, "address": "123 Main St" }

# DELETE /orders/{order_id}
# DELETE /orders


# Entity: ORDER

# CREATE: POST
# READ:   GET
# UPDATE: PATCH, PUT
# DELETE: DELETE

# STATUS CODES
# 1XX
# 2XX SUCCESS
# 3XX
# 4XX CLIENT ERROR
# 5XX SERVER ERROR


# /posts/{post_id}/comments EQUIVALENT
# /posts

# /posts/comments EQUIVALENT
# /reviews/comments
# /product/comments

# /comments/post EQUIVALENT
# /comments/reviews
# /comments/prouct

# /comments?post_id=10 EQUIVALENT














# • GET /reviews/{id}/comments
# • GET /posts/{id}/comments

# • GET /comments
# • GET /comments?reviewId={id}


