# E-commerce API

This is a backend API for an e-commerce platform built with Django and Django REST Framework (DRF). It provides endpoints for managing users, products, and categories, as well as authentication and filtering capabilities.

## Features

- **User Management**: Custom user model with extended fields such as `othername`, `phone_number`, `address`, and `image_url`.
- **Product Management**: CRUD operations for products with fields like name, description, price, stock quantity, and category.
- **Category Management**: Manage product categories with fields like name, description, and image.
- **Authentication**: JWT-based authentication using `rest_framework_simplejwt`.
- **Filtering and Searching**: Filter products by price range, search by name, and order by fields.
- **Pagination**: Paginated responses for product listings.
- **Rate Limiting**: Scoped rate throttling for product-related endpoints.
- **CORS Support**: Configured for development with multiple frontend origins.


## Installation

1. Clone the repository:
   ```Bash
   git clone <repository-url>
   cd ecommerce_api
   ``` 

## Create and activate a virtual environment:
```Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install dependencies
```Bash
pip install -r requirements.txt
```
## Create Super User
```Bash
python manage.py createsuperuser
```
## Run the development server
```Bash
python manage.py runserver
```

## API Endpoints


### Users
POST /users/register/: Register a new user.
POST users/login/: Login and Obtain JWT tokens.
POST users/token/refresh/: Refresh JWT tokens.


### Products
GET /api/products/: List all products.
POST /api/products/: Create a new product.
GET /api/products/detail/<id>/: Retrieve a product by ID.
PUT /api/products/update/<id>/: Update a product by ID.
DELETE /api/products/delete/<id>/: Delete a product by ID.


### Categories
GET /api/categories/: List all products.
POST /api/categories/: Create a new product.
GET /api/categories/detail/<id>/: Retrieve a product by ID.
PUT /api/categories/update/<id>/: Update a product by ID.
DELETE /api/categories/delete/<id>/: Delete a product by ID.


## Configuration

Environment Variables
Update the SECRET_KEY in settings.py for production.
Configure ALLOWED_HOSTS for your deployment.

## Media Files
Media files are stored in the images/ directory. Update MEDIA_URL and MEDIA_ROOT in settings.py as needed.


## CORS
Allowed origins are configured in the CORS_ALLOWED_ORIGINS setting.

## Dependencies
Django 5.2.x
Django REST Framework
Django Simple JWT
Django Filters
Django CORS Headers