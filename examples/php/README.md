# Advanced E-commerce Search - PHP Example

### Description:

This is a PHP example setup for the Advanced E-commerce Search tool. It demonstrates how to integrate the search functionality with a PHP backend. This example is designed to be easily adaptable to your e-commerce platform's existing PHP setup.

## Setup:

1. **Database Configuration:**
   Update the database connection details in index.php with your database credentials.

2. **Database Schema:**
   Import the db.sql file into your MySQL database to create the necessary tables and keys.

3. **Run the PHP Server:**
   We recommend using XAMPP to run your PHP server. Place this project in the htdocs directory of XAMPP, and navigate to http://localhost/path/to/your/project to access the API endpoints.

### Example Endpoints

1. **Products:**
   **GET /?api=products** - Retrieves all products with category and subcategory names.

2. **Categories:**
   **GET /?api=categories** - Retrieves all categories.

3. **Subcategories:**
   **GET /?api=subcategories** - Retrieves all subcategories.

## Note

When using this PHP example, make sure to update the `main.py` configuration for your Python application to match the PHP server URLs. Specifically, change the following URLs:

```python
products_url = 'http://localhost/path/to/your/project/?api=products'
categories_url = 'http://localhost/path/to/your/project/?api=categories'
subcategories_url = 'http://localhost/path/to/your/project/?api=subcategories'
```

For improved performance and ease of use, we highly recommend using Node.js for setting up the API backend. Node.js offers better scalability, asynchronous processing, and a rich ecosystem of libraries and tools.
