
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
