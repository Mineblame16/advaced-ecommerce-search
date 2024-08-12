Here’s the `README.md` for the Node.js example:

---

# Advanced E-commerce Search - Node.js Example

## Description

This is a Node.js example setup for the Advanced E-commerce Search tool. It provides a straightforward integration with your e-commerce platform using a Node.js backend. This example demonstrates how to set up a REST API to interact with the search functionality of the tool.

## Setup

1. **Install Dependencies:**
   Ensure you have Node.js and npm installed. Navigate to the project directory and install the required dependencies:
   ```bash
   npm install
   ```

2. **Database Configuration:**
   Update the `.env` file with your database credentials. Make sure it matches your MySQL setup:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_passwords
   DB_NAME=advaced_ecommerce_search
   ```

3. **Run the Server:**
   Start the Node.js server:
   ```bash
   node index.js
   ```
   By default, the server will run on `http://localhost:3000`.

## Example Endpoints

- **Products:**
  `GET /api/products` - Retrieves all products with category and subcategory names.

- **Categories:**
  `GET /api/categories` - Retrieves all categories.

- **Subcategories:**
  `GET /api/subcategories` - Retrieves all subcategories.

## Why Node.js?

We highly recommend using Node.js for the API backend due to its non-blocking I/O model, which provides better performance and scalability compared to other technologies. Node.js's vast ecosystem of libraries and its asynchronous nature make it an excellent choice for handling high traffic and complex data operations efficiently.