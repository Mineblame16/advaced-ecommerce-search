-- Create the database
CREATE DATABASE IF NOT EXISTS advaced_ecommerce_search;
USE advaced_ecommerce_search;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create subcategories table
CREATE TABLE IF NOT EXISTS subcategories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    features TEXT,
    image1 VARCHAR(255),
    image2 VARCHAR(255),
    image3 VARCHAR(255),
    image4 VARCHAR(255),
    image5 VARCHAR(255),
    category_id INT,
    subcategory_id INT,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (subcategory_id) REFERENCES subcategories(id)
);

-- Insert sample data into categories table
INSERT INTO categories (name) VALUES
('Electronics'),
('Home Appliances'),
('Clothing'),
('Books');

-- Insert sample data into subcategories table
INSERT INTO subcategories (name) VALUES
('Mobile Phones'),
('Laptops'),
('Televisions'),
('Washing Machines'),
('Men\'s Clothing'),
('Women\'s Clothing'),
('Fiction'),
('Non-Fiction');

-- Insert sample data into products table
INSERT INTO products (title, description, features, image1, image2, image3, image4, image5, category_id, subcategory_id, price) VALUES
('Smartphone', 'Latest model with high performance.', '5G, 8GB RAM, 128GB Storage', 'https://placehold.co/600x400', 'https://example.com/image2.jpg', NULL, NULL, NULL, 1, 1, 699.99),
('Laptop', 'High-end laptop with excellent specs.', '16GB RAM, 512GB SSD', 'https://placehold.co/600x400', 'https://example.com/image2.jpg', 'https://example.com/image3.jpg', NULL, NULL, 1, 2, 1299.99),
('Washing Machine', 'Efficient washing machine with multiple programs.', 'Front Load, 7kg Capacity', 'https://placehold.co/600x400', NULL, NULL, NULL, NULL, 2, 4, 499.99),
('Men\'s T-Shirt', 'Comfortable cotton t-shirt.', 'Available in multiple sizes and colors.', 'https://placehold.co/600x400', NULL, NULL, NULL, NULL, 3, 5, 19.99),
('Fiction Book', 'Bestselling fiction novel.', 'A thrilling read.', 'https://placehold.co/600x400', NULL, NULL, NULL, NULL, 4, 7, 12.99);

-- Add additional constraints or indexes if needed
